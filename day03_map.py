from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ("北京",1),
    ("内蒙古",2),
    ("新疆",3),
    ("江苏",4),
    ("广西",5),
    ("安徽",6),
]
map.add("测试中国地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True,
    is_piecewise=True,
    pieces=[
        {"min":1,"max":9,"label":"1-9","color":"red"},
        {"min":10,"max":99,"label":"10-99","color":"blue"},
        {"min":100,"max":500,"label":"100-500","color":"yellow"},
    ]
    )
)
map.render()