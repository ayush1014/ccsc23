from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import json


def get_movie_titles(data_records):
    titles = []
    for item in data_records:
        titles.append(item["Title"])
    return titles

data = []
with open("HighestHolywoodGrossingMovies.json") as json_file:
    data = json.load(json_file)
    
app = Dash(__name__)

app.layout = html.Div(children = [
    dcc.Markdown(
        id = "title",
        children = "## Movie Sales Dashboard"
    ),

    dcc.Dropdown(
        id = "titles_dropdown",
        options = get_movie_titles(data),
        value = ["Star Wars: Episode VII - The Force Awakens (2015)","Avengers: Endgame (2019)"],
        multi = True
    ),

    dcc.Graph(
        id = "movie_sales_bar_graph",
        figure = px.bar(data,x="Title",y='World Sales (in $)',title="Movie Sales")
    )
])


@app.callback(
    Output("movie_sales_bar_graph","figure"),
    Input("titles_dropdown","value")
)
def update_sales_graph(selected_title_list):
    records_to_display = []
    for movie_record in data:
        if movie_record["Title"] in selected_title_list:
            records_to_display.append(movie_record)
    new_fig = px.bar(records_to_display,x="Title",y='World Sales (in $)',title="Movie Sales")
    return new_fig

if __name__ == '__main__':
    app.run_server(debug=True)