import pandas
import numpy
from constants.constants import DAY
from functions.graph import graph_config
def main_dashboard():
    # Graficos TMD.
    graph_config(
        name='Tempo Médio de Descarga',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Graficos VAM.
    graph_config(
        name='Veiculos Atendidos por Mês',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TMC.
    graph_config(
        name='Tempo Médio de Conferência',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico POE.
    graph_config(
        name='Produtividade por Operador de Equipe',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TUA.
    graph_config(
        name='Taxa de Utilização de Agendamentos',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TRP.
    graph_config(
        name='Taxa de Retorno de Produto',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico IDE.
    graph_config(
        name='Indice de disponibilidade de estoque',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }             
        )
    )
    # Grafico TIO.
    graph_config(
        name='Taxa de Itens Obsoletos',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }              
        )           
    ) 

    graph_config(
        name='Custo de Manutenção de Estoque',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )     