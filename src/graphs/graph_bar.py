import plotly.express
def graph_bar(
    data_frame,
    x,
    y,
    title:str=None,
    subtitle:str=None, 
    color=None,
    color_discrete_sequence=None, 
    barmode='relative',
    opacity=1.0,
    xaxis_title=None,
    yaxis_title=None, 
    text_auto=False,
    hover_name=None,
    width=None,
    height=None,
    template=None,
    show_legend=True,
    legend_title=None,
    orientation='v',
):
    """
    ``Grafico Barra com plotly express``

    Parâmetros:
    - ``data_frame``: DataFrame com os dados
    - ``x``: Coluna para o eixo x
    - ``y``: Coluna para o eixo y
    - ``title``: Título do gráfico
    - ``subtitle``: Subtítulo do gráfico
    - ``color``: Coluna para diferenciação por cor
    - ``color_discrete_sequence``: Lista de cores para as barras
    - ``barmode``: 'relative' (empilhado), 'group' (agrupado) ou 'overlay'.
        - No modo 'relativo', as barras são empilhadas acima de zero para valores positivos e abaixo de zero para valores negativos.
        - No modo 'sobrelay', as barras são desenhadas umas sobre as outras.
        - No modo 'grupo', as barras são colocadas ao lado umas das outras.
    - ``opacity``: Opacidade das barras (0.0 a 1.0)
    - ``xaxis_title``: Título personalizado para o eixo x
    - ``yaxis_title``: Título personalizado para o eixo y
    - ``text_auto``: Exibir valores nas barras (True/False ou formato como '.2f')
    - ``hover_name``: Coluna para mostrar no hover
    - ``width``: Largura do gráfico
    - ``height``: Altura do gráfico
    - ``template``: Template do Plotly ('plotly', 'plotly_white', 'plotly_dark', etc.)
    - ``show_legend``: Mostrar legenda (True/False)
    - ``legend_title``: Título personalizado para a legenda
    - ``orientation``: Orientação ('v' para vertical ou 'h' para horizontal)
    """
    fig = plotly.express.bar(
        data_frame=data_frame,
        x=x,
        y=y,
        title=title,
        subtitle=subtitle, 
        color=color,
        color_discrete_sequence=color_discrete_sequence, 
        barmode=barmode,
        opacity=opacity,
        text_auto=text_auto,
        hover_name=hover_name,
        width=width,
        height=height,
        template=template,
        orientation=orientation,
    )
    fig.update_layout(
        showlegend=show_legend,
        legend_title_text=legend_title,
        xaxis=dict(
            title=xaxis_title,
            showgrid=True,
            gridcolor="#000000"
        ),
        yaxis=dict(
            title=yaxis_title,
            showgrid=True,
            gridcolor="#000000",
            range=[0, 100]
        )

    )
    return fig