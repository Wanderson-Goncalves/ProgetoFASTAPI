from ast import Str
from email.policy import default
from random import choices
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Boolean, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#cria a conexão do seu banco de dados
db = create_engine("sqlite:///banco.db")

#cria a base do banco de dados

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(50), nullable=False)
    email = Column("email", String(100), nullable=False)
    senha = Column("senha", String(20), nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin  
        

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    # STATUS_PEDIDOS =(
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )
    
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String(20), default= "PENDENTE")
    usuario_id = Column("usuario_id", Integer, ForeignKey('usuarios.id'), nullable=False)
    preco = Column("preco", Float, nullable=False)
    # itens

    def __init__(self, status, usuario_id, preco=0):
        self.status = status
        self.usuario_id = usuario_id
        self.preco = preco  
    

class ItemPedido(Base):
    __tablename__ = 'itens_pedido'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String(50), nullable=False)
    tamanho = Column("tamanho", String(11), nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido_id = Column("pedido_id", Integer, ForeignKey('pedidos.id'), nullable=False)
    
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido_id):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido_id = pedido_id 
