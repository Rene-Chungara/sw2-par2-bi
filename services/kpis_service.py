from fastapi.responses import JSONResponse
import pandas as pd
from config.db import get_database

def get_ventas_mensuales():
    db = get_database()
    ventas = list(db.ventas.find())

    df = pd.DataFrame(ventas)
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
    df["mes"] = df["fecha_venta"].dt.to_period("M")
    df["monto_total"] = df["cantidad_vendida"] * df["precio_venta_unitario"]

    resumen = df.groupby("mes")["monto_total"].sum().reset_index()
    resumen["mes"] = resumen["mes"].astype(str)

    return JSONResponse(content={
        "labels": resumen["mes"].tolist(),
        "values": resumen["monto_total"].round(2).tolist()
    })

def get_kpis_globales():
    try:
        db = get_database()
        ventas = pd.DataFrame(list(db.ventas.find()))
        finanzas = pd.DataFrame(list(db.finanzas.find()))

        total_ventas = (ventas["cantidad_vendida"] * ventas["precio_venta_unitario"]).sum()
        total_productos = ventas["cantidad_vendida"].sum()

        finanzas["margen"] = finanzas["precio_venta_unitario"] - finanzas["costo_unitario"]
        margen_promedio = finanzas["margen"].mean()

        return JSONResponse(content={
            "total_ventas": round(float(total_ventas), 2),
            "total_productos_vendidos": int(total_productos),
            "margen_promedio": round(float(margen_promedio) / finanzas["precio_venta_unitario"].mean(), 4)
        })
    except Exception as e:
        print("❌ ERROR en get_kpis_globales:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})
