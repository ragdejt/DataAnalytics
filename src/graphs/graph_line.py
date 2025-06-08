
import plotly.express
def graph_line(
    df,
    x,
    y,
    title=None,
    subtitle=None,
    color=None,
    line_group=None,
    hover_name=None,
    hover_data=None,
    facet_row=None,
    facet_col=None,
    width=None,
    height=600,
    line_shape='linear',
    color_discrete_sequence=None,
    color_continuous_scale=None,
    line_dash=None,
    markers=False,
    symbol=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    template="plotly_dark",
):
    """
    ``Cria um gráfico de linha interativo com múltiplas opções de personalização.``

    Parâmetros:
    - ``df``: DataFrame contendo os dados
    - ``x``: Nome da coluna para eixo x
    - ``y``: Nome da coluna para eixo y
    - ``title``: Título do gráfico
    - ``subtitle``: Subtítulo do gráfico
    - ``color``: Coluna para diferenciação por cor
    - ``line_group``: Coluna para agrupamento de linhas
    - ``hover_name``: Coluna para exibir ao passar o mouse
    - ``hover_data``: Lista de colunas adicionais para tooltip
    - ``facet_row``: Coluna para facetar por linhas
    - ``facet_col``: Coluna para facetar por colunas
    - ``width``: Largura do gráfico em pixels
    - ``height``: Altura do gráfico em pixels
    - ``line_shape``: Formato da linha 
        - ``linear``
        - ``spline``: Linha curva suavizada
        - ``hv``: Horizontal then Vertical
        - ``vh``: Vertical then Horizontal
        - ``hvh``: Horizontal-Vertical-Horizontal
        - ``vhv``: Vertical-Horizontal-Vertical
    - ``color_discrete_sequence``: Sequência de cores para categorias
    - ``color_continuous_scale``: Escala de cores para valores contínuos
    - ``line_dash``: Coluna para estilo de traço da linha
    - ``markers``: Se True, mostra marcadores nos pontos
    - ``symbol``: Coluna para diferenciação por símbolo
    - ``log_x``: Se True, escala logarítmica no eixo x
    - ``log_y``: Se True, escala logarítmica no eixo y
    - ``range_x``: Intervalo do eixo x [min, max]
    - ``range_y``: Intervalo do eixo y [min, max]
    - ``template``: Template do gráfico
        - "plotly"
        - "plotly_dark"
        - "plotly_white"
    """
    fig = plotly.express.line(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        subtitle=subtitle,
        color=color,
        line_group=line_group,
        hover_name=hover_name,
        hover_data=hover_data,
        facet_row=facet_row,
        facet_col=facet_col,
        width=width,
        height=height,
        line_shape=line_shape,
        color_discrete_sequence=color_discrete_sequence,
        color_continuous_scale=color_continuous_scale,
        line_dash=line_dash,
        markers=markers,
        symbol=symbol,
        log_x=log_x,
        log_y=log_y,
        range_x=range_x,
        range_y=range_y,
        template=template
    )
    return fig