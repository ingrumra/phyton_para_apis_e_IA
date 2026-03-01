
from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class CancerMamaIn(BaseModel):
    # Identificadores / geografía
    codigo_sspm: Optional[int] = Field(None, ge=0)
    cod_divipola: Optional[int] = Field(None, ge=0)
    ciudad: Optional[str] = None
    dpto: Optional[str] = None

    # Demografía
    edad: Optional[int] = Field(None, ge=0, le=120)
    sexo: Optional[str] = None
    tip_ss: Optional[str] = None
    per_etn: Optional[str] = None

    # Fechas (en Semana 2 asumimos formato ISO si llegan por API)
    fec_not: Optional[date] = None
    fec_con: Optional[date] = None
    ini_sin: Optional[date] = None
    fec_pro_co: Optional[date] = None
    fec_res_bi: Optional[date] = None

    # Variables clínicas (texto/categorías)
    res_biops9: Optional[str] = None
    grad_histo: Optional[str] = None


class CancerMamaOut(CancerMamaIn):
    """
    Output tipado. Por ahora es equivalente al input.
    En semanas siguientes podrás agregar campos derivados (flags de calidad, etc.).
    """
    pass