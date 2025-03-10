# Import packages
import micropip
import asyncio
async def install_package():
    await micropip.install("dash_ag_grid")

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Plotly graphs
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='column-options'),
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
    ),
    dcc.Graph(figure=fig, id='graph1')
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='column-options', component_property='value')
)
def update_graph(col_chosen):
    # dff = df[df.country.isin(['Albania', 'Romania', 'Iran', 'India', 'Egypt', 'Australia'])]
    # fig = px.histogram(dff, x='continent', y=col_chosen, histfunc='avg',
    #                    pattern_shape='country', labels={'country': 'Countries'})
    fig = px.scatter(df, x='gdpPercap', y='lifeExp', range_x=[10000, 40000], color='continent')
    fig.update_traces(showlegend=False)
    fig.update_layout(font_size=22)
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
