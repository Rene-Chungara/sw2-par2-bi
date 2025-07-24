from config.db import get_database
import pandas as pd
from fastapi.responses import JSONResponse

def productos_mas_vendidos_chart():
    db = get_database()
    ventas = list(db.ventas.find())

    df = pd.DataFrame(ventas)

    # Agrupar por producto y sumar las cantidades vendidas
    resumen = df.groupby("producto_id")["cantidad_vendida"].sum().sort_values(ascending=False).head(10)

    # Devolver datos como labels y values
    return JSONResponse(content={
        "labels": resumen.index.tolist(),
        "values": resumen.values.tolist()
    })


def margen_ganancia_chart():
    db = get_database()
    finanzas = list(db.finanzas.find())

    df = pd.DataFrame(finanzas)
    df["margen"] = df["precio_venta_unitario"] - df["costo_unitario"]

    # Agrupar por producto y obtener margen promedio
    resumen = df.groupby("producto_id")["margen"].mean().reset_index()

    return JSONResponse(content={
        "labels": resumen["producto_id"].tolist(),
        "values": resumen["margen"].round(2).tolist()  # puedes redondear si lo deseas
    })
