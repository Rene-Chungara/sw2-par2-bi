from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.kpis_service import get_ventas_mensuales, get_kpis_globales
from services.charts_service import productos_mas_vendidos_chart, margen_ganancia_chart
from models.schemas import ChartResponse
import os

app = FastAPI()

# CORS: Permitir frontend desde Vercel y desarrollo local
origins = [
    "https://sw2-par2-front.vercel.app",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Endpoints con manejo de errores ===

@app.get("/api/kpis/ventas-mensuales")
def kpi_ventas():
    try:
        print("🔍 Ejecutando get_ventas_mensuales()")
        return get_ventas_mensuales()
    except Exception as e:
        print("❌ Error en get_ventas_mensuales:", e)
        return {"error": str(e)}

@app.get("/api/charts/productos-mas-vendidos", response_model=ChartResponse)
def chart_productos():
    try:
        print("🔍 Ejecutando productos_mas_vendidos_chart()")
        return productos_mas_vendidos_chart()
    except Exception as e:
        print("❌ Error en productos_mas_vendidos_chart:", e)
        return {"error": str(e)}

@app.get("/api/charts/margen-ganancia", response_model=ChartResponse)
def chart_margen():
    try:
        print("🔍 Ejecutando margen_ganancia_chart()")
        return margen_ganancia_chart()
    except Exception as e:
        print("❌ Error en margen_ganancia_chart:", e)
        return {"error": str(e)}

@app.get("/api/kpis/resumen")
def kpi_resumen():
    try:
        print("🔍 Ejecutando get_kpis_globales()")
        return get_kpis_globales()
    except Exception as e:
        print("❌ Error en get_kpis_globales:", e)
        return {"error": str(e)}

# === Ejecutar servidor local o en Railway ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
