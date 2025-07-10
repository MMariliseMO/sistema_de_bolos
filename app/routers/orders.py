#Rota de pedidos
from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
async def read_users():
    return{"mensagem": "Listar pedidos"}

#URL final: http://seu_servidor/pedidos