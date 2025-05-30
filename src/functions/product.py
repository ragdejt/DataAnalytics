from decorators.timer import timer
from models.produto import Produto
from database.database import SessionLocal
from sqlalchemy.exc import PendingRollbackError


@timer
def add_product(
    name:str,
    description:str,
    category:str,
    price:float,
    quantity:int,
    height:float,
    width:float,
    length:float,
    weight:float,
    active:bool = True,
):
    """
    Adiciona um produto ao banco de dados.

    Args:
        name (str): Nome do produto.
        description (str): Descrição do produto.
        category (str): Categoria do produto.
        price (float): Preço do produto.
        quantity (int): Quantidade do produto.
        height (float): Altura do produto.
        width (float): Largura do produto.
        length (float): Comprimento do produto.
        weight (float): Peso do produto.
        active (bool): Se o produto está ativo ou não.
    """
    try:
        with SessionLocal() as session:
            session.add(Produto(
                Nome=name,
                Descricao=description,
                Categoria=category,
                Preco=price,
                Quantidade=quantity,
                Altura=height,
                Largura=width,
                Comprimento=length,
                Peso=weight,
                Ativo=active
            ))
            session.commit()
    except PendingRollbackError:
        session.rollback()
    finally:
        session.close()
