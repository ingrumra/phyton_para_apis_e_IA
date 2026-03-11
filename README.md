# Python para APIs e IA (2026-1)

# Python para APIs e IA — Fase 1 (Semanas 1–4)

## Aportes del proyecto

Este proyecto aporta una base funcional para abordar el tratamiento de datos en un contexto aplicado de salud, tomando como caso de trabajo un archivo de registros sobre cáncer de mama correspondiente a PIII 2023. Más que operar sobre datos abstractos, el repositorio se construyó sobre una base real que presenta problemas frecuentes en escenarios institucionales: columnas vacías, nombres de variables poco estandarizados, fechas en formato textual, campos categóricos que requieren homogeneización y estructuras que deben prepararse antes de poder ser consultadas de manera confiable. La lógica de limpieza implementada permite precisamente responder a este tipo de dificultades mediante funciones reutilizables de depuración y transformación. 


En este sentido, el principal aporte del proyecto consiste en conectar tres niveles que suelen trabajarse por separado: primero, la depuración y estandarización del archivo fuente; segundo, la validación estructurada de los registros; y tercero, la exposición de esos datos mediante una API consumible desde una interfaz web. Esta articulación resulta especialmente valiosa porque transforma una base originalmente cruda en un insumo más consistente para consulta, visualización y análisis posterior. La implementación en FastAPI y la organización modular del proyecto muestran esa transición desde el procesamiento tabular hacia una arquitectura orientada a servicios. 


Adicionalmente, el proyecto deja ver un aprendizaje progresivo en términos de diseño técnico. El repositorio no solo contiene funciones de limpieza, sino también una estructura por rutas, componentes separados para lógica de negocio y una capa de interacción frontend. Por ello, el aporte no debe leerse únicamente como un ejercicio de programación, sino como la construcción de una base técnica que podría evolucionar hacia procesos más robustos de monitoreo de calidad del dato, analítica descriptiva y automatización de reportes en salud.

## Objetivo (qué se construyó)
- **Semana 1:** Pipeline de limpieza con **Pandas** y funciones puras (módulo `cleaning.py`), + script de EDA que genera un CSV limpio.   
- **Semana 2:** **Esquemas Pydantic** (Input/Output) y endpoint de demostración `POST /validate` (validación y tipado)  
- **Semana 3:** Mini-app **Flask** con endpoints `GET /health`, `POST /echo`, `POST /clean` usando la misma lógica de limpieza.   
- **Semana 4:** Migración a FastAPI con versionado bajo `/api/v1` (por ejemplo `GET /api/v1/health`, `POST /api/v1/clean`, etc.).
-(ASGI) con `/docs` y endpoints tipados; se prepara la migración de lógica de limpieza hacia FastAPI y validación estricta c  

## Alcance

El proyecto cubre el desarrollo de una base funcional para trabajar con datos estructurados en Python, desde su carga y limpieza inicial hasta su exposición mediante endpoints. Incluye una etapa de exploración y depuración con pandas, una capa de validación, una API principal en FastAPI y una interfaz web conectada a dicha API. Además, conserva rastros del proceso de evolución técnica, incluyendo una fase previa implementada en Flask.

No obstante, es importante señalar que el repositorio aún se encuentra en desarrollo. En particular, la ruta /api/v1/stats devuelve valores estáticos de ejemplo para alimentar el frontend, por lo que esta parte debe entenderse como una demostración funcional y no como una capa analítica definitiva conectada al dataset real.

## Dataset
Se trabaja con: `cancer_mama_piii_2023_raw.csv` (cáncer de mama, PIII 2023).

**Importante:** el archiv y no se versiona en GitHub por buenas prácticas (puede ser grande o sensible).  
El CSV usa separador `;`, por eso la carga se hace con `read_csv(sep=";")`. :contentReference[oaicite:14]{index=14}itorio (resumen)
- `src/app/` → API FastAPI + lógica core
  - `src/app/core/cleaning.py` → funciones puras de limpieza
  - `src/app/core/schemas.py` → modelos Pydantic (Input/Output)
  - `src/app/api/` → routers (health, validate, etc.) definición de rutas y endpoints.
- `src/flask_app/` → mini‐app Flask 
- `scripts/` → scripts de exploración y procesamiento.
- `tests/` → pruebas automatizadas (pytest)
- `data/raw/` y `data/processed/` → rutas para datos crudos y procesados, no versionados en GitHub por buenas prácticas.

## Exploración y limpieza de datos

El proyecto parte de un archivo CSV crudo que se carga usando pandas. A partir de allí, se implementan funciones orientadas a resolver problemas frecuentes de calidad de datos: eliminación de columnas totalmente vacías, normalización de nombres de columnas, tipificación de variables numéricas y transformación de fechas en formato español. También se incorpora un perfil básico de valores faltantes por columna.

## Validación de datos

Luego de la limpieza inicial, el proyecto incorpora una capa de validación para mejorar la consistencia de los registros que entran y salen del sistema. Esto resulta especialmente importante cuando los datos dejan de ser manipulados solo como tablas y pasan a ser consumidos como objetos a través de endpoints.

## Construcción de la API

La aplicación principal está desarrollada en FastAPI y registra rutas para estado del sistema, demostración de esquema, limpieza de registros y carga de archivos CSV. La app además incorpora configuración CORS abierta para facilitar las pruebas desde un frontend estático en entorno de desarrollo.

Entre las funcionalidades ya visibles en el código se encuentran:

GET / para confirmar que la API está corriendo.

POST /api/v1/clean para limpiar una lista de registros enviada en JSON y devolver número de filas, faltantes, columnas y registros transformados.

POST /api/v1/clean-file para cargar un archivo CSV, inferir delimitador, aplicar limpieza y devolver registros, columnas y estadísticas básicas por columna.

GET /api/v1/stats como endpoint de apoyo para el dashboard, actualmente con datos de ejemplo.

## Interfaz web y visualización

El README actual indica que el proyecto puede levantarse junto con un dashboard, lo que muestra que el repositorio no se queda en la capa backend, sino que también contempla una interfaz de interacción para explorar los resultados. Esta integración es importante porque traduce la lógica de limpieza y consulta en una experiencia más visible y verificable para el usuario.

## Organización y evolución del proyecto

El repositorio también evidencia una progresión pedagógica y técnica: primero se trabajó la limpieza de datos, luego la validación, después una miniapp en Flask y finalmente la migración hacia FastAPI. Esa trayectoria es valiosa porque deja ver el aprendizaje incremental y la reorganización del código hacia una arquitectura más mantenible.

## Valor del caso de estudio

La base de cáncer de mama utilizada en este proyecto permitió trabajar con un caso realista de datos en salud, donde el desafío no radica únicamente en almacenar registros, sino en prepararlos para su uso analítico y operativo. Precisamente por ello, el proyecto adquiere valor como ejercicio aplicado: parte de un archivo con limitaciones reales de estructura y calidad, y avanza hacia una solución que busca limpiar, validar y exponer la información de forma más ordenada y reutilizable. Este caso de estudio demuestra que incluso una arquitectura sencilla puede aportar significativamente cuando se orienta a resolver problemas concretos de calidad y disponibilidad del dato.

