from wsgiref.simple_server import demo_app
from fastapi import APIRouter


order_router = APIRouter(prefix="/pedidos",tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    
    """
    Essa é a rota padrão de pedidos do nosso sistema.
    """
    return {"mensagem":"você acessou a rota de pedidos"}