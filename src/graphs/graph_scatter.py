import plotly.express
def graph_scatter(
    data_frame,
    x,
    y,
    title:str=None,
    color=None,
    color_discrete_sequence=None,
    color_continuous_scale=None,
    symbol=None,
    size=None,
    size_max=None,
    opacity=1.0,
    xaxis_title=None,
    yaxis_title=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    width=None,
    height=None,
    template=None,
    show_legend=True,
    legend_title=None,
    trendline=None,
    trendline_options=None,
    marginal_x=None,
    marginal_y=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    render_mode='auto',
    category_orders=None,
    labels=None,
    orientation=None,
    symbol_sequence=None,
    symbol_map=None,
    animation_frame=None,
    animation_group=None,
):
    """
    ``Cria um gráfico de dispersão (scatter) interativo com múltiplas opções de personalização.``

    Parâmetros:
    - ``data_frame``: DataFrame com os dados
    - ``x``: Coluna para eixo x
    - ``y``: Coluna para eixo y
    - ``title``: Título principal do gráfico
    - ``subtitle``: Subtítulo (opcional)
    - ``color``: Coluna para diferenciação por cores
    - ``color_discrete_sequence``: Sequência de cores para categorias
    - ``color_continuous_scale``: Escala de cores para valores contínuos
    - ``symbol``: Coluna para diferenciação por símbolos
    - ``size``: Coluna para tamanho dos marcadores
    - ``size_max``: Tamanho máximo dos marcadores
    - ``opacity``: Opacidade dos marcadores (0-1)
    - ``xaxis_title``: Título do eixo x
    - ``yaxis_title``: Título do eixo y
    - ``hover_name``: Coluna para destaque no hover
    - ``hover_data``: Colunas adicionais no tooltip
    - ``custom_data``: Dados extras para callbacks
    - ``text``: Coluna para texto nos pontos
    - ``width``: Largura do gráfico
    - ``height``: Altura do gráfico
    - ``template``: Template de layout
    - ``show_legend``: Mostrar legenda
    - ``legend_title``: Título da legenda
    - ``trendline``: Adicionar linha de tendência ('ols', 'lowess', etc)
    - ``trendline_options``: Opções para linha de tendência
    - ``marginal_x``: Gráfico marginal no eixo x ('histogram', 'box', etc)
    - ``marginal_y``: Gráfico marginal no eixo y
    - ``marginal_dist``: Tipo de distribuição marginal
    - ``log_x``: Escala log no eixo x
    - ``log_y``: Escala log no eixo y
    - ``range_x``: Intervalo do eixo x
    - ``range_y``: Intervalo do eixo y
    - ``render_mode``: Modo de renderização ('auto', 'webgl', 'svg')
    - ``category_orders``: Ordem de categorias
    - ``labels``: Rótulos personalizados
    - ``orientation``: Orientação do gráfico
    - ``symbol_sequence``: Sequência de símbolos
    - ``symbol_map``: Mapeamento de símbolos
    - ``animation_frame``: Coluna para animação por frames
    - ``animation_group``: Coluna para agrupamento de animação
    """
    fig = plotly.express.scatter(
        data_frame=data_frame,
        x=x,
        y=y,
        color=color,
        color_discrete_sequence=color_discrete_sequence,
        color_continuous_scale=color_continuous_scale,
        symbol=symbol,
        size=size,
        size_max=size_max,
        opacity=opacity,
        hover_name=hover_name,
        hover_data=hover_data,
        custom_data=custom_data,
        text=text,
        width=width,
        height=height,
        template=template,
        trendline=trendline,
        trendline_options=trendline_options,
        marginal_x=marginal_x,
        marginal_y=marginal_y,
        log_x=log_x,
        log_y=log_y,
        range_x=range_x,
        range_y=range_y,
        render_mode=render_mode,
        category_orders=category_orders,
        labels=labels,
        orientation=orientation,
        symbol_sequence=symbol_sequence,
        symbol_map=symbol_map,
        animation_frame=animation_frame,
        animation_group=animation_group,
    )
    
    fig.update_layout(
        showlegend=show_legend,
        legend_title_text=legend_title,
        title=title,
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