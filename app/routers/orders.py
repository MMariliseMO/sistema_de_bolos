#Rota de pedidos
from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
async def listar_pedidos():
    return("mensagem:" "Listar pedidos")

#URL final: http://seu_servidor/pedidos