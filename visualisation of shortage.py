import heapq
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie
import csv

#define dataset
df_vis_shortage = pd.read_csv('shortage.csv')

#define the elements that need to be drawn: map, histogram, and pie chart into a function "get_year_chart" at the same time.
def get_year_chart(year: int):
    map_data = df_vis_shortage[['Country',str(year)]].values.tolist()
    min_data, max_data = (
        min([d[1] for d in map_data]),
        max([d[1] for d in map_data]),
    )
    map_chart = (
        Map()
        .add(
            series_name="",
            data_pair=map_data,
            maptype="world",
            label_opts=opts.LabelOpts(is_show=False),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Water Shortage Map and Prediction from 1988",
                subtitle="Total internal renewable water resources per capita (m3/inhab/yr)",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                #formatter=JsCode(
                #    """function(params) {
                #    if ('value' in params.data) {
                #        return params.data.value[2] + ': ' + params.data.value[0];
                #    }
                #}"""
                #),
            ),
          visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["Abundance", "Shortage"],
                is_piecewise=True, 
                pieces=[
                    {"min":200,"max":5000,"label":"200~5000","color":"#FE2E2E"},
                    {"min":5001,"max":10000,"label":"5001~10000","color":"#F78181"},
                    {"min":10001,"max":20000,"label":"10001~20000","color":"#F7F981"},
                    {"min":20001,"max":30000,"label":"20001~30000","color":"#F5DA81"},
                    {"min":30001,"max":40000,"label":"30001~40000","color":"#E1F5A9"},
                    {"min":40001,"max":50000,"label":"40001~50000","color":"#BCF5A9"},
                    {"min":50001,"max":80000,"label":"50001~80000","color":"#A9F5E1"},
                    {"min":80001,"max":240000,"label":"80001+","color":"#A9E2F3"},
                ],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            #pos_top= "middle",  #分段位置
            #pos_left="left",
            #orient="vertical"
            #split_number=10  #分成10个区间
        ),
        )
    )
    
    map_data_top=sorted(map_data,key=lambda x:x[1],reverse=True)[0:9]
    bar_x_data = [x[0] for x in map_data_top]

    bar_y_data = [{"name": x[0], "value": x[1]} for x in map_data_top]
    bar = (
        Bar()
        .add_xaxis(xaxis_data=bar_x_data)
        .add_yaxis(
            series_name="",
            yaxis_index=1,
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b}: {c}"
            ),
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["Abundance", "Shortage"],
                is_piecewise=True, 
                pieces=[
                    {"min":200,"max":5000,"label":"200~5000","color":"#FE2E2E"},
                    {"min":5001,"max":10000,"label":"5001~10000","color":"#F78181"},
                    {"min":10001,"max":20000,"label":"10001~20000","color":"#F7F981"},
                    {"min":20001,"max":30000,"label":"20001~30000","color":"#F5DA81"},
                    {"min":30001,"max":40000,"label":"30001~40000","color":"#E1F5A9"},
                    {"min":40001,"max":50000,"label":"40001~50000","color":"#BCF5A9"},
                    {"min":50001,"max":80000,"label":"50001~80000","color":"#A9F5E1"},
                    {"min":80001,"max":240000,"label":"80001+","color":"#A9E2F3"},
                ],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=f"{str(year)} ",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#fff"),
                            ),
                        ),
                    ],
                )
            ],
        )
    )
    
    pie_data = sorted(map_data,key=lambda x:x[1], reverse=True)
    pie = (
        Pie()
        .add(
            series_name="",
            data_pair=pie_data,
            radius=["12%", "20%"],
            center=["75%", "85%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
        .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="70%", pos_bottom="5"
            ),
        )
        .add(pie, grid_opts=opts.GridOpts())
        .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart

    # Add timeline and Render Webpage
time_list = [1992, 1997, 2002, 2007,2012, 2017, 2022]
timeline = Timeline(
    init_opts=opts.InitOpts(width="1250px", height="850px", theme=ThemeType.DARK)
)

timelabel = ['1988-1992', '1993-1997', '1998-2002', '2003-2007', '2008-2012', '2013-2017', 'Predicted']

for y in time_list:
    g = get_year_chart(year=y)
    timeline.add(g, time_point=timelabel[time_list.index(y)])

timeline.add_schema(
    orient="vertical",
    is_auto_play=True,
    is_inverse=True,
    play_interval=5000,
    pos_left="null",
    pos_right="5",
    pos_top="20",
    pos_bottom="20",
    width="50",
    label_opts=opts.LabelOpts(is_show=True, color="#fff"),
)

timeline.render("water_shortage_from_1988.html")