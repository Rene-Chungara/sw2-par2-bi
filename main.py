from fastapi import FastAPI
from services.kpis_service import get_ventas_mensuales
from services.charts_service import productos_mas_vendidos_chart, margen_ganancia_chart
from models.schemas import KPI, ChartResponse
from fastapi.middleware.cors import CORSMiddleware
from services.kpis_service import get_kpis_globales


app = FastAPI()

# Permitir CORS para Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/kpis/ventas-mensuales")
def kpi_ventas():
    return get_ventas_mensuales()

@app.get("/api/charts/productos-mas-vendidos", response_model=ChartResponse)
def chart_productos():
    return productos_mas_vendidos_chart()

@app.get("/api/charts/margen-ganancia", response_model=ChartResponse)
def chart_margen():
    return margen_ganancia_chart()

@app.get("/api/kpis/resumen")
def kpi_resumen():
    return get_kpis_globales()
