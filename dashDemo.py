from dash import Dash, html, dcc
import plotly.express as px
import json


data = []
with open("HighestHolywoodGrossingMovies.json") as json_file:
    data = json.load(json_file)

app = Dash(__name__)

app.layout = html.Div(children = [
    dcc.Markdown(
        id = "title",
        children = "## Movie Sales Dashboard"
    ),

    dcc.Graph(
        id = "movie_sales_bar_graph",
        figure = px.bar(data,x="Title",y='World Sales (in $)',title="Movie Sales")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)