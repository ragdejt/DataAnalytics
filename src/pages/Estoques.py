import streamlit
import numpy
import pandas
from config.page_config import page_config
from functions.table import edit_table
from graphs.graph_bar import graph_bar
from graphs.graph_line import graph_line
from graphs.graph_scatter import graph_scatter
from graphs.graph_area import graph_area
from graphs.graph_pie import graph_pie
# Grafico IDE.
graph_data = pandas.DataFrame(data={
        'Dia':range(1,31),
        'Janeiro':numpy.random.randint(low=1, high=100, size=30),
        'Fevereiro':numpy.random.randint(low=1, high=100, size=30),
        'Março':numpy.random.randint(low=1, high=100, size=30),
        'Abril':numpy.random.randint(low=1, high=100, size=30),
        'Maio':numpy.random.randint(low=1, high=100, size=30),
        'Junho':numpy.random.randint(low=1, high=100, size=30),
        'Julho':numpy.random.randint(low=1, high=100, size=30),
        'Agosto':numpy.random.randint(low=1, high=100, size=30),
        'Setembro':numpy.random.randint(low=1, high=100, size=30),
        'Outubro':numpy.random.randint(low=1, high=100, size=30),
        'Novembro':numpy.random.randint(low=1, high=100, size=30),
        'Dezembro':numpy.random.randint(low=1, high=100, size=30)
    }
)
estoques = page_config(
    title='Estoques',
    option_sidebar=['Estoque'])

if streamlit.session_state['login']:
    match estoques:
        case 'Estoque':
            streamlit.subheader(':green[Editar estoque]', divider='green')
            edit_table('Estoques')
        case _:
            column1, column2 = streamlit.columns(2)
            with column1:
                fig1=graph_line(
                    data_frame=graph_data,
                    x='Dia',
                    y=['Janeiro',
                        'Fevereiro',
                        'Março',
                        'Abril',
                        'Maio',
                        'Junho',
                        'Julho',
                        'Agosto',
                        'Setembro',
                        'Outubro',
                        'Novembro',
                        'Dezembro',
                    ]
                    
                )
                streamlit.plotly_chart(figure_or_data=fig1, use_container_width=True)
                fig3=graph_scatter(
                    data_frame=graph_data,
                    x='Dia',
                    y=['Janeiro',
                        'Fevereiro',
                        'Março',
                        'Abril',
                        'Maio',
                        'Junho',
                        'Julho',
                        'Agosto',
                        'Setembro',
                        'Outubro',
                        'Novembro',
                        'Dezembro',
                    ]
                )
                streamlit.plotly_chart(figure_or_data=fig3, use_container_width=True)
                fig5=graph_pie(
                    data_frame=graph_data,
                    names='Dia',
                    values='Janeiro'
                )
                streamlit.plotly_chart(figure_or_data=fig5, use_container_width=True)
            with column2:
                fig2=graph_bar(
                    data_frame=graph_data,
                    x='Dia',
                    y=['Janeiro',
                        'Fevereiro',
                        'Março',
                        'Abril',
                        'Maio',
                        'Junho',
                        'Julho',
                        'Agosto',
                        'Setembro',
                        'Outubro',
                        'Novembro',
                        'Dezembro',
                    ],
                    barmode='group'
                )
                streamlit.plotly_chart(figure_or_data=fig2, use_container_width=True)
                fig4 = graph_area(
                    data_frame=graph_data,
                    x='Dia',
                    y=['Janeiro',
                        'Fevereiro',
                        'Março',
                        'Abril',
                        'Maio',
                        'Junho',
                        'Julho',
                        'Agosto',
                        'Setembro',
                        'Outubro',
                        'Novembro',
                        'Dezembro',
                    ]
                )
                streamlit.plotly_chart(figure_or_data=fig4, use_container_width=True)
