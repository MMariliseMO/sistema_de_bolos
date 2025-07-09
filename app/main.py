from fastapi import FastAPI 
from app.routers import orders, users

app = FastAPI(title="Sistema de Pedidos de Bolos") 

app.include_router(users.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return {"message" : "Bem-vindo(a) à minha API!"}