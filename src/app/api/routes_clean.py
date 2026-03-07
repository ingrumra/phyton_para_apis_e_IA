from typing import List
import pandas as pd
from fastapi import APIRouter

from ..core.schemas import CancerMamaIn, CancerMamaOut
from ..core.cleaning import clean_dataframe, profile_missing

router = APIRouter()

@router.post("/clean", response_model=dict)
def clean_endpoint(records: List[CancerMamaIn]):
    """
    Week 4: Endpoint FastAPI que valida con Pydantic y aplica limpieza.
    Recibe una lista de registros (JSON array).
    """
    df = pd.DataFrame([r.model_dump() for r in records])
    df_clean = clean_dataframe(df)

    out_records = [
        CancerMamaOut(**row).model_dump()
        for row in df_clean.to_dict(orient="records")
    ]

    return {
        "n": len(out_records),
        "missing": profile_missing(df_clean),
        "records": out_records,
    }
