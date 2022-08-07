# We need to fetch the dataframe of this motion detector program to this script
from motion_detector import df
# import the plotting interface of Bokeh
from bokeh.plotting import figure, show, output_file
# hoverTool is a method expects some data, so that it will display them when user hovers the mouse over these quadrants
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds=ColumnDataSource(df)

# create the figure object
p=figure(x_axis_type='datetime',height=100, width=500, sizing_mode = "scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

# create a hover object, whihc has a tooptips parameter
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
# add this tool using the add_tools() method
p.add_tools(hover)

# plot a glyph in the figure we create
q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("Graph1.html")
show(p)
