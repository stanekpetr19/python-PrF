import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),                                        # pro zápis se dá použít markdown
                                                                    # bude potřeba pro domácí úkol
    html.Div(children='''
        Data o Titaniku
    '''),

    dcc.Dropdown(                                                   # dropdown pro výběr možností
    options=[
        {'label': 'Cena lístků podle třídy', 'value': 'fare_class'},
        {'label': 'Věk cestujících podle třídy', 'value': 'age_class'},
    ],
    value='fare_class'
    ),
            
    dcc.RadioItems(                                                 # příklad přepínače
    options=[
        {'label': 'Histogram', 'value': 'hist'},
        {'label': 'Boxplot', 'value': 'boxplot'}
    ],
    value='hist'
    ),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Bar(x = [1, 2, 3], y = [4, 1, 2], name ='Cherbourg'),
                go.Bar(x = [1, 2, 3], y = [2, 4, 5], name = 'Queenstown'),
                go.Bar(x = [1, 2, 3], y = [3, 2, 3], name = 'Southampton')
            ],
            'layout': {
                'title': 'Nástupní místo dle třídy jizdenky', "xaxis" : {"title" : "Třída jízdenky"}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()