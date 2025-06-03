from models.estoque import Estoque
from database.database import SessionLocal
from constants.constants import CATEGORIAS
def add_stock():
    with SessionLocal() as session:  
        for id_estoque in CATEGORIAS:
            for rua in range(1, 11):
                for predio in range(1, 11):
                    for andar in range(0, 5):
                        for lado in ['A', 'B']:
                            new_stock = Estoque(
                                Estoque=id_estoque,
                                Rua=rua,
                                Predio=predio,
                                Andar=andar,
                                Lado=lado,
                                Produto=0,
                                Quantidade=0
                            )
                            session.add(new_stock)  
        session.commit()  