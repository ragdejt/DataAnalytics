import plotly.express

def graph_pie(
    data_frame,
    names,
    values,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    category_orders=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    opacity=None,
    hole=None
):
    """
    """
    fig = plotly.express.pie(
        data_frame=data_frame,
        names=names,
        values=values,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
        facet_row_spacing=facet_row_spacing,
        facet_col_spacing=facet_col_spacing,
        color_discrete_sequence=color_discrete_sequence,
        color_discrete_map=color_discrete_map,
        hover_name=hover_name,
        hover_data=hover_data,
        custom_data=custom_data,
        category_orders=category_orders,
        labels=labels,
        title=title,
        subtitle=subtitle,
        template=template,
        width=width,
        height=height,
        opacity=opacity,
        hole=hole
    )
    return fig