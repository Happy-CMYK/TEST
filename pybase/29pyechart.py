# 折线图

# from Tools.demo.spreadsheet import center
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts, VisualMapOpts
#
#
#
# line = Line ()
# line.add_xaxis ( ["中国", "美国", "英国"] )
# line.add_yaxis ( "GDP", [30, 20, 10] )
#
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#
#
#
# line.render ()


# 地图
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map ()
data = [
    ("北京市", "99"),
    ("上海市", "199999"),
    ("湖南省", "299"),
    ("台湾省", "199"),
    ("安徽省", "299"),
    ("广州省", "399"),
    ("湖北省", "599"),
]
map.add ( "测试地图", data, 'china' )

# 设置全局变量
map.set_global_opts (
    visualmap_opts=VisualMapOpts (
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", 'color': "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", 'color': "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", 'color': "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", 'color': "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", 'color': "#CC3333"},
            {"min": 1000, "label": "10000以上", 'color': "#990033"}
        ]
    )
)

map.render ()

# 基础柱状图
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

bar1 = Bar ()

bar1.add_xaxis ( ['中国', '美国', '英国'] )

bar1.add_yaxis ( "GDP", [30, 20, 10], label_opts=LabelOpts ( position='right' ) )

# 反转xy轴
bar1.reversal_axis ()

bar2 = Bar ()

bar2.add_xaxis ( ['中国', '美国', '英国'] )

bar2.add_yaxis ( "GDP", [80, 40, 30], label_opts=LabelOpts ( position='right' ) )

# 反转xy轴
bar2.reversal_axis ()

timeline = Timeline ()

timeline.add ( bar1, "2021年GDP" )
timeline.add ( bar2, "2022年GDP" )

timeline.add_schema (
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render ( "基础柱状图-时间线.html" )

my_list = [["a", 33], ['b', 55], ['c', 11]]


def choose_sort_key(element):
    return element[1]


# my_list.sort ( key=choose_sort_key, reverse=True )
my_list.sort ( key=lambda element: element[1], reverse=True )
print ( my_list )







# 散点图
from pyecharts import options as opts
from pyecharts.charts import Scatter
import pandas as pd
from pyecharts.commons.utils import JsCode

def scatter_render():
    df = pd.DataFrame(
        {
            '年龄':[18,23,28,30,32,40,19,45],
            '信用积分':[630,710,730,740,680,700,650,800],
            '姓名':['小明','彦祖','德华','大聪明','rose','tom','小丽丽','刘能']
        }
    )

    # 年龄的排序
    df.sort_values('年龄',inplace=True,ascending=True)
    c = (
        Scatter()
        .add_xaxis(df.年龄.values.tolist())
        .add_yaxis(
            '信用积分',
            df[['信用积分','姓名']].values.tolist(),
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    # js中函数的写法   通过定义js的回调函数自定义组合的标签显示
                    "function(params){return params.value[2];}"
                )
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='散点图图例'),
            #     设置数据的范围和数据的连续性
            xaxis_opts=opts.AxisOpts(
                type_='value',
                min_=18
            ),
            yaxis_opts=opts.AxisOpts(
                min_=600
            )
        )

    )
    return c
scatter_render().render('散点图显示.html')

