from typing import List
import pandas as pd
from fastapi import APIRouter, UploadFile, File

from ..core.schemas import CancerMamaIn, CancerMamaOut
from ..core.cleaning import clean_dataframe, profile_missing

router = APIRouter()

@router.post("/clean", response_model=dict)
async def clean_records(payload: List[dict]):
    """Limpia un listado de registros enviado en el body.

    Conserva compatibilidad con el esquema de pruebas: devolvemos
    número total (`n`), `missing` por columna, plus registros/columns.
    """
    df = pd.DataFrame(payload)
    cleaned = clean_dataframe(df)
    return {
        "n": len(cleaned),
        "missing": profile_missing(cleaned),
        "records": cleaned.to_dict(orient="records"),
        "columns": list(cleaned.columns),
    }


@router.post("/clean-file")
async def clean_file(file: UploadFile = File(...)):
    """Recibe un CSV y retorna los registros limpios"""
    try:
        df = pd.read_csv(file.file, sep=";")
    except Exception as e:
        return {"error": f"No se pudo leer el CSV: {e}"}
    cleaned = clean_dataframe(df)
    # genera estadísticas básicas por columna (conteo de valores únicos)
    stats = {col: int(cleaned[col].nunique()) for col in cleaned.columns}
    return {
        "records": cleaned.to_dict(orient="records"),
        "columns": list(cleaned.columns),
        "stats": stats,
    }
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
