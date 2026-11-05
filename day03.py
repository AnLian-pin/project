from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line=Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,40,20])
line.set_global_opts(
    title_opts=TitleOpts(title="各个国家GDP折线图",pos_left="center"),
)
line.render()