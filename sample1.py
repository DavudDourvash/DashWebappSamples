import asyncio
import micropip
from plotly.graph_objs import Figure


async def install_package():
    await micropip.install("dash_ag_grid")

asyncio.run(install_package())
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# Plotly graphs
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='lifeExp', id = 'my-div'),
    html.Hr(),
    # dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id = 'column-options'),
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        dashGridOptions={"rowSelection" : "single"}
    ),
    dcc.Graph(figure=fig, id='graph1')
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Output(component_id= 'my-div', component_property='children'),
    Input(component_id='column-options', component_property='value'),
    Input(component_id = 'grid', component_property = 'selectedRows')
)
def update_graph(col_chosen, my_row):
    print(my_row)
    print(my_row[0]['country'])
    dff = df[df.country == my_row[0]['country']]
    print(dff.head())
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig, col_chosen


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
