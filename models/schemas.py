from pydantic import BaseModel
from typing import List

class KPI(BaseModel):
    label: str
    value: float

class ChartResponse(BaseModel):
    title: str
    image_url: str
