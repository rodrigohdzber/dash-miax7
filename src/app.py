import pandas as pd
import dash
from dash import dcc   #para los graficos.
from dash import html  #para poner h1, div como hicimos al crear la pagina web
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import api_bme
from api_bme import APIBMEHandler
#DE MOMENTO EL FICHERO RUN NO VALE PARA NADA.
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets) #creas un objeto que se llama app
#aquí estamos creando la web por decirlo así estaría vacía. y los estilos
#y luego tendrá distintas propiedades como layout que es para ir rellenando la web igual que haciamos en html

markets = ["DAX", "IBEX", "EUROSTOXX"]

ah = api_bme.APIBMEHandler(market='IBEX')
ticker_data = ah.get_close_data_ticker("SAN")

ticker_master = ah.get_ticker_master()
tcks= list(ticker_master.ticker)
dropdown_values = [{'label': tck, 'value': tck} for tck in tcks]
    

fig = px.line(ticker_data)

app.layout = html.Div(children=[  #PONEMOS LOS ATRIBUTOS A LA APP(WEB) UN TITULO, UN SEGUNDO TITULO, Y UN GRAFICO.
    html.H1(
        children='MIAX Data Explorer',
    ),
    html.H5(
        children='mIAx API',
    ),
    dcc.Dropdown(
        id='markets',
        options=[
            {'label': 'IBEX', 'value': 'IBEX'},
            {'label': 'DAX', 'value': 'DAX'},
            {'label': 'EUROSTOXX', 'value': 'EUROSTOXX'}
        ],
        value='IBEX' #value por defecto
    ),
    dcc.Dropdown(
        id='tickers',
    ),
    dcc.Graph(
        id='graph',
        #figure=fig aqui ya no hace falta está puesto abajo
    )
])

@app.callback(
    Output("tickers", "options"),
    Input("markets", "value"))   #poniendo el mercado que cambie los tickers que tienen
def change_index(selected_index):
    ah.market = selected_index
    ticker_master = ah.get_ticker_master()
    tcks= list(ticker_master.ticker)
    dropdown_values = [{'label': tck, 'value': tck} for tck in tcks]
    
    return dropdown_values

@app.callback( #con este callback cuando seleccionas un indice ya te marca directamente sus tickers
    Output("tickers", "value"),
    Input("tickers", "options"))
def change_value_ticker(new_options):  #new options sería dropdownvalues podriamos poder dos outputs arriba 
    return new_options[0]["value"]

@app.callback( 
    Output("graph", "figure"),
    Input("tickers", "value"))
def change_graph(ticker):  
    ticker_data = ah.get_data_ticker(ticker)
    #fig = px.line(ticker_data["close"])
    fig = go.Figure(go.Candlestick(
        x = ticker_data.index,
        open = ticker_data["open"],
        high = ticker_data["high"],
        low = ticker_data["low"],
        close = ticker_data["close"]
    ))  
    return fig
    

if __name__ == "__main__":  #ejecuta la aplicacion.
    app.run_server(host="0.0.0.0", debud=False, port=8080)  #QUE CORRA LA APLICACION DE ARRIBA.
    


