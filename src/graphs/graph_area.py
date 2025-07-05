import plotly.express

def graph_area(
    data_frame,
    x,
    y,
    xaxistitle=None,
    yaxistitle=None,
    show_legend=True,
    legend_title=None,
    line_group=None,
    color=None,
    pattern_shape=None,
    symbol=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    orientation=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    line_shape=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    groupnorm=None,
    ):
    """
    ``Cria um gráfico de área interativo com múltiplas opções de personalização.``

    Parâmetros:
    - ``data_frame``: DataFrame contendo os dados
    - ``x``: Coluna para eixo x
    - ``y``: Coluna para eixo y
    - ``xaxistitle``: Título do eixo x
    - ``yaxistitle``: Título do eixo y
    - ``show_legend``: Mostrar legenda (True/False)
    - ``legend_title``: Título da legenda
    - ``line_group``: Coluna para agrupamento de linhas
    - ``color``: Coluna para diferenciação por cores
    - ``symbol``: Coluna para símbolos dos pontos
    - ``hover_name``: Coluna para destaque no hover
    - ``hover_data``: Lista de colunas adicionais no hover
    - ``custom_data``: Colunas para dados extras
    - ``text``: Coluna para texto nos pontos
    - ``facet_row``: Coluna para facetas em linhas
    - ``facet_col``: Coluna para facetas em colunas
    - ``facet_col_wrap``: Número máximo de colunas de facetas
    - ``facet_row_spacing``: Espaçamento entre linhas de facetas
    - ``facet_col_spacing``: Espaçamento entre colunas de facetas
    - ``animation_frame``: Coluna para animação por frames
    - ``animation_group``: Coluna para agrupamento de animação
    - ``category_orders``: Ordem personalizada de categorias
    - ``labels``: Dicionário para renomear rótulos
    - ``orientation``: Orientação do gráfico ('v' ou 'h')
    - ``color_discrete_sequence``: Sequência de cores discretas
    - ``color_discrete_map``: Mapeamento de cores discretas
    - ``symbol_sequence``: Sequência de símbolos
    - ``symbol_map``: Mapeamento de símbolos
    - ``markers``: Exibir marcadores nos pontos
    - ``log_x``: Escala logarítmica no eixo x
    - ``log_y``: Escala logarítmica no eixo y
    - ``range_x``: Intervalo do eixo x
    - ``range_y``: Intervalo do eixo y
    - ``line_shape``: Formato da linha ('linear', 'spline', etc)
    - ``title``: Título do gráfico
    - ``template``: Template de layout
    - ``width``: Largura do gráfico
    - ``height``: Altura do gráfico
    - ``groupnorm``: Normalização de grupo (None, 'fraction', 'percent')
    - ``stackgroup``: Coluna para agrupamento de stack
    """
    fig=plotly.express.area(
        data_frame=data_frame,
        x=x,
        y=y,
        line_group=line_group,
        color=color,
        pattern_shape=pattern_shape,
        symbol=symbol,
        hover_name=hover_name,
        hover_data=hover_data,
        custom_data=custom_data,
        text=text,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
        facet_row_spacing=facet_row_spacing,
        facet_col_spacing=facet_col_spacing,
        animation_frame=animation_frame,
        animation_group=animation_group,
        category_orders=category_orders,
        labels=labels,
        color_discrete_sequence=color_discrete_sequence,
        color_discrete_map=color_discrete_map,
        pattern_shape_sequence=pattern_shape_sequence,
        pattern_shape_map=pattern_shape_map,
        symbol_sequence=symbol_sequence,
        symbol_map=symbol_map,
        markers=markers,
        orientation=orientation,
        groupnorm=groupnorm,
        log_x=log_x,
        log_y=log_y,
        range_x=range_x,
        range_y=range_y,
        line_shape=line_shape,
        title=title,
        subtitle=subtitle,
        template=template,
        width=width,
        height=height
    )    
    fig.update_layout(
        title=title,
        showlegend=show_legend,
        legend_title_text=legend_title,
        xaxis=dict(
            title=xaxistitle,
            showgrid=True,
            gridcolor="#000000"
        ),
        yaxis=dict(
            title=yaxistitle,
            showgrid=True,
            gridcolor="#000000"
        )
    )
    
    return fig

