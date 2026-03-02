from app.api.routes_health import router as health_router
from fastapi import FastAPI
from app.api.routes_health import router as health_router
from app.api.routes_clean import router as clean_router

app = FastAPI(title="Python para APIs e IA", version="0.1.0")
app.include_router(health_router, tags=["health"])

from app.api.routes_schema_demo import router as schema_router

app = FastAPI(title="Python para APIs e IA", version="0.1.0")
app.include_router(health_router, tags=["health"])
app.include_router(schema_router, tags=["week2"])

app.include_router(clean_router, tags=["clean"])