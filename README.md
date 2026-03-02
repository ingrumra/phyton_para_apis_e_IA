# Python para APIs e IA (2026-1)

# Python para APIs e IA — Fase 1 (Semanas 1–4)

Este repositorio implementa la **Fase 1 (Semanas 1–4)** del curso: entorno reproducible, selección de dataset, limpieza en Pandas con funciones puras, esquemas Pydantic, mini‐app Flask con endpoints y migración a FastAPI con documentación automática y validación. 

## Objetivo (qué se construyó)
- **Semana 1:** Pipeline de limpieza con **Pandas** y funciones puras (módulo `cleaning.py`), + script de EDA que genera un CSV limpio.   
- **Semana 2:** **Esquemas Pydantic** (Input/Output) y endpoint de demostración `POST /validate` (validación y tipado)  
- **Semana 3:** Mini-app **Flask** con endpoints `GET /health`, `POST /echo`, `POST /clean` usando la misma lógica de limpieza.   
-(ASGI) con `/docs` y endpoints tipados; se prepara la migración de lógica de limpieza hacia FastAPI y validación estricta c  

## Dataset
Se trabaja con: `cancer_mama_piii_2023_raw.csv` (cáncer de mama, PIII 2023).

**Importante:** el archiv y no se versiona en GitHub por buenas prácticas (puede ser grande o sensible).  
El CSV usa separador `;`, por eso la carga se hace con `read_csv(sep=";")`. :contentReference[oaicite:14]{index=14}itorio (resumen)
- `src/app/` → API FastAPI + lógica core
  - `src/app/core/cleaning.py` → funciones puras de limpieza
  - `src/app/core/schemas.py` → modelos Pydantic (Input/Output)
  - `src/app/api/` → routers (health, validate, etc.)
- `src/flask_app/` → mini‐app Flask (semana 3)
- `scripts/` → evidencia de EDA/limpieza (semana 1)
- `tests/` → pruebas automatizadas (pytest)
- `data/raw/` y `data/processed/` → datos (ignorados por `.gitignore`)

## Requisitos
- Python 3.11.x
- Windows PowerShell (comandos listos para PowerShell)
- Dependencias instalables vía `requirements.txt`

## Instalación (Windows / PowerShell)
1) Crear y activar entorno virtual :
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1