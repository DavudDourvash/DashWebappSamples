import micropip
import asyncio

async def install_package():
        await micropip.install("dash-bootstrap-components")

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.ZEPHYR]
)

app.layout = dbc.Container([
    html.H1("Dash Bootstrap Alerts"),
    dbc.Alert("Hello, Bootstrap!", className="m-5", is_open=True, duration=4000),
    dbc.Button("Primary", color="primary", className="me-1")
])

if __name__ == "__main__":
    app.run_server()