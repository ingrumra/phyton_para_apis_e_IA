from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["stats"])

# Esta ruta devuelve estadísticas ficticias de casos por comuna.
# En una versión real leerías los datos de un CSV o base de datos.
@router.get("/stats")
def get_stats():
    """Retorna una lista de diccionarios con `comuna` y `cantidad`.
    Este ejemplo usa valores estáticos para que el frontend pueda consumirlos.
    """
    return [
        {"comuna": 1, "cantidad": 12},
        {"comuna": 2, "cantidad": 5},
        {"comuna": 3, "cantidad": 8},
        {"comuna": 4, "cantidad": 20},
        {"comuna": 5, "cantidad": 15},
    ]
