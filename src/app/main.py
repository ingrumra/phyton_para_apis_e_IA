from fastapi import FastAPI

from .api.routes_health import router as health_router
from .api.routes_clean import router as clean_router
from .api.routes_schema_demo import router as schema_router
from .api.routes_stats import router as stats_router

app = FastAPI(title="Python para APIs e IA", version="0.1.0")

# CORS (permite peticiones desde el frontend estático o cualquier origen en desarrollo)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rutas básicas (versionadas)
app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(schema_router, prefix="/api/v1", tags=["week2"])
app.include_router(clean_router, prefix="/api/v1", tags=["clean"])
app.include_router(stats_router)  # ya define su propio prefix en el router

@app.get("/")
def root():
    return {"message": "API running. Go to /docs"}
