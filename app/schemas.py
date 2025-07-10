from pydantic import BaseModel, EmailStr
from datetime import datetime, date

#Criar Pedido:
class CreateOrders(BaseModel):
    nome_cliente: str
    telefone: str
    tipo_bolo: str
    data_entrega: date
    observacao: str

#Cadastro de usuário:
class CreateUsers(BaseModel):
    nome: str
    email: EmailStr
    senha: str

#Login do Usuário:
class LoginUsers(BaseModel):
    email: EmailStr
    senha: str
