
from fastapi import APIRouter
from ..core.schemas import CancerMamaIn, CancerMamaOut

router = APIRouter()

@router.post("/validate", response_model=CancerMamaOut)
def validate_schema(payload: CancerMamaIn):
    """
    Endpoint de demostración: valida entrada con Pydantic y devuelve el mismo payload tipado.
    """
    return CancerMamaOut(**payload.model_dump())