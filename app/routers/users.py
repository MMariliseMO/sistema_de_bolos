#Rotas de Login/Cadastro
from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/login")
async def login():
    return{"mensagem:" "Login do usuário"}

#URL final: http: //seu_servidor/usuarios/login