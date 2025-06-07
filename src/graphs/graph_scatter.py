import plotly.express
def graph_scatter(
    df,
    x,
    y,
    title: str,
    subtitle: str = None, 
    color=None,
    color_discrete_sequence=None, 
    symbol=None,
    size=None,
    opacity=1.0,
    xaxis_title=None,
    yaxis_title=None, 
    hover_name=None,
    width=None,
    height=None,
    template=None,
    show_legend=True,
    legend_title=None,
    trendline=None,
    marginal_x=None,
    marginal_y=None,
    log_x=False,
    log_y=False,
    size_max=None,
):
    """
    ``Gráfico de Dispersão (Scatter Plot) com plotly express``

    Parâmetros:
    - ``df``: DataFrame com os dados
    - ``x``: Coluna para o eixo x
    - ``y``: Coluna para o eixo y
    - ``title``: Título do gráfico
    - ``subtitle``: Subtítulo do gráfico
    - ``color``: Coluna para diferenciação por cor
    - ``color_discrete_sequence``: Lista de cores para os pontos
    - ``symbol``: Coluna para diferenciação por símbolo
    - ``size``: Coluna para diferenciação por tamanho dos pontos
    - ``opacity``: Opacidade dos pontos (0.0 a 1.0)
    - ``xaxis_title``: Título personalizado para o eixo x
    - ``yaxis_title``: Título personalizado para o eixo y
    - ``hover_name``: Coluna para mostrar no hover
    - ``width``: Largura do gráfico
    - ``height``: Altura do gráfico
    - ``template``: Template do Plotly ('plotly', 'plotly_white', 'plotly_dark', etc.)
    - ``show_legend``: Mostrar legenda (True/False)
    - ``legend_title``: Título personalizado para a legenda
    - ``trendline``: Adicionar linha de tendência ('ols', 'lowess', None)
    - ``marginal_x``: Gráfico marginal no eixo x ('histogram', 'box', 'violin', 'rug', None)
    - ``marginal_y``: Gráfico marginal no eixo y ('histogram', 'box', 'violin', 'rug', None)
    - ``log_x``: Usar escala logarítmica no eixo x (True/False)
    - ``log_y``: Usar escala logarítmica no eixo y (True/False)
    - ``size_max``: Tamanho máximo dos pontos quando 'size' é usado
    """ 
    fig = plotly.express.scatter(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        subtitle=subtitle,
        color=color,
        color_discrete_sequence=color_discrete_sequence,
        symbol=symbol,
        size=size,
        opacity=opacity,
        hover_name=hover_name,
        width=width,
        height=height,
        template=template,
        log_x=log_x,
        log_y=log_y,
        size_max=size_max,
        trendline=trendline,
        marginal_x=marginal_x,
        marginal_y=marginal_y,
    )
    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        showlegend=show_legend,
        legend_title=legend_title,
    )
    return fig