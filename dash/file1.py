# import dash
# import dash_html_components as html

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1('First application'),
#     html.Div(
#         html.P("First Sentence")
#     ),
#     html.Table([
#         html.Thead(
#         html.Tr([
#             html.Th('header_1'),
#             html.Th('header_2')
#         ])
#         ),
#         html.Tbody(
#         html.Tr([
#             html.Td('my_column_1'),
#             html.Td('my_column_2')
#         ])
#         )
#     ])
# ])

# if __name__ == '__main__':
#     app.run_server(debug = True, host = "0.0.0.0")



# import dash
# import dash_html_components as html

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     html.H1('First application', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
#     html.Div(
#         html.P("First Sentence"),
#         style = {'display': 'inline-block','width': '50%'}
#     ),
#     html.Table([
#         html.Thead(
#         html.Tr([
#             html.Th('header_1'),
#             html.Th('header_2')
#         ], style={'color': "darkOrange"})
#         ),
#         html.Tbody(
#         html.Tr([
#             html.Td('my_column_1'),
#             html.Td('my_column_2')
#         ])
#         )
#     ], style = {'display': 'inline-block','width': '50%'})
# ], style = {'backgroundColor': 'beige'})

# if __name__ == '__main__':
#     app.run_server(debug = True, host='0.0.0.0')


# import dash
# import dash_core_components as dcc

# app = dash.Dash(__name__)

# app.layout = dcc.Dropdown(
#   id = 'dropdown',
#   options=[
#     {'label':'life expendancy', 'value': 'lifeExp'},
#     {'label':'population', 'value': 'pop'}
#     ],
#     value = 'pop', # Valeur affichée par défaut dans le menus.
#     multi = False # Spécifier si c'est un menu dropdown à multiple choix ou non.
# )
# if __name__ == '__main__' :
#     app.run_server(debug=True, host='0.0.0.0')



# import dash
# import dash_core_components as dcc

# app = dash.Dash(__name__)

# app.layout = dcc.Slider(
#   id = 'Slider_1',
#   min = 0,
#   max = 10, 
#   marks = {i: str(i) for i in range(10)},
#   value = 5
# )
# if __name__ == '__main__' :
#     app.run_server(debug=True,host='0.0.0.0')


# import dash
# import dash_core_components as dcc
# import plotly.express as px 

# # Création de la figure 

# df = px.data.gapminder().query("year == 2002")
# fig = px.scatter(df, x="gdpPercap", y="lifeExp",
#                         color="continent",
#                         size="pop",
#                         hover_name="country")

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__,external_stylesheets = external_stylesheets)

# app.layout = dcc.Graph(id= 'Premier graphe',
#                       figure= fig)

# if __name__ == '__main__':
#   app.run_server(debug=True, host = '0.0.0.0')




import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px  

df = px.data.gapminder()
df_1 = df[df["year"] == 2002]

# Création de la figure plotly
fig = px.scatter(df_1, x="gdpPercap", y="lifeExp",
                        color="continent",
                        hover_name="country")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
  html.H1('API Dash', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
  html.Div(dcc.Dropdown(id = 'Dropdown',
                        options= [{'label': 'life expandency', 'value': 'lifeExp'},
                                  {'label': 'population', 'value': 'pop'}],
                        value= 'lifeExp'
  )),
  html.Div(dcc.Graph(id='graph_1',
                      figure=fig)),

  html.Div(dcc.Slider(id = 'slider_1',
                      min = df['year'].min(),
                      max = df['year'].max(),
                      marks={str(i): str(i) for i in df['year'].unique()},
                      step = None))
], style = {'background' : 'beige'})

if __name__ == '__main__':
  app.run_server(debug=True,host = '0.0.0.0')