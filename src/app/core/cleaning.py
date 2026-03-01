
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, Tuple

import pandas as pd


SPANISH_MONTHS = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
    "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12
}


def parse_spanish_date(value: Any) -> Optional[date]:
    """
    Convierte fechas tipo '3-ene-2023' a datetime.date.
    Retorna None si el valor está vacío o es inválido.
    """
    if value is None:
        return None
    s = str(value).strip().lower()
    if s in {"", "nan", "none"}:
        return None

    # Formato esperado: d-mes-aaaa (ej: 3-ene-2023)
    m = re.match(r"^(\d{1,2})-([a-zñ]{3})-(\d{4})$", s)
    if not m:
        return None

    day = int(m.group(1))
    mon_txt = m.group(2)
    year = int(m.group(3))

    month = SPANISH_MONTHS.get(mon_txt)
    if month is None:
        return None

    try:
        return date(year, month, day)
    except ValueError:
        return None


def load_raw_csv(path: str) -> pd.DataFrame:
    """
    Carga el CSV crudo. Importante: el separador es ';'.
    """
    return pd.read_csv(path, sep=";", engine="python")


def drop_fully_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina columnas completamente vacías (como Unnamed: xx).
    """
    keep_cols = [c for c in df.columns if not df[c].isna().all()]
    return df[keep_cols].copy()


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza nombres: quita espacios, baja a minúsculas, elimina '_' finales.
    """
    new_cols = []
    for c in df.columns:
        c2 = c.strip().lower()
        c2 = re.sub(r"_+$", "", c2)  # quita underscores finales
        new_cols.append(c2)
    out = df.copy()
    out.columns = new_cols
    return out


def profile_missing(df: pd.DataFrame) -> Dict[str, int]:
    """
    Conteo de valores faltantes por columna (NaN/None).
    """
    return df.isna().sum().to_dict()


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpieza básica:
    - elimina columnas vacías
    - normaliza nombres
    - estandariza strings
    - parsea fechas (formato español)
    - convierte edad/códigos a numérico cuando aplica
    """
    df = drop_fully_empty_columns(df)
    df = normalize_column_names(df)

    out = df.copy()

    # strip/lower en columnas de texto (si existen)
    text_cols = ["ciudad", "dpto", "sexo", "tip_ss", "per_etn", "res_biops9", "grad_histo"]
    for c in text_cols:
        if c in out.columns:
            out[c] = out[c].astype(str).str.strip().str.lower().replace({"nan": None})

    # conversiones numéricas
    if "edad" in out.columns:
        out["edad"] = pd.to_numeric(out["edad"], errors="coerce").astype("Int64")

    if "cod_divipola" in out.columns:
        out["cod_divipola"] = pd.to_numeric(out["cod_divipola"], errors="coerce").astype("Int64")

    if "codigo_sspm" in out.columns:
        out["codigo_sspm"] = pd.to_numeric(out["codigo_sspm"], errors="coerce").astype("Int64")

    # fechas: parse español
    date_cols = ["fec_not", "fec_con", "ini_sin", "fec_pro_co", "fec_res_bi", "fecha_corte", "fecha_reporte_web"]
    for c in date_cols:
        if c in out.columns:
            out[c] = out[c].apply(parse_spanish_date)

    return out