import pandas as pd
import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html
from dash.dependencies import Output,Input
import dash_table
import plotly.graph_objs as go

df = pd.read_csv("nba_2013.csv")
dfnba =  df[(df["bref_team_id"] != "TOT") & (df["pos"]!= "G")]
# print(dfnba.head(5))

#retirer les tuples où la variable bref_team_id a pour valeur "TOT" et la variable "pos" a pour valeur G.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id = 'page-content')
])

index_page = html.Div([
    html.H1('NBA 2013', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Button(dcc.Link('Camparatif de joueurs', href='/page-1')),
    html.Br(),
    html.Button(dcc.Link("Comparatif d'équipes", href='/page-2')),
    html.Br(),

])


# page1 camparatif de joueurs


# Div Rookie
dfrookie = dfnba[dfnba["age"]<24]
div_rookie = html.Div([
    html.H1('Rookie', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Div(dcc.Dropdown(id = 'player-Dropdown-rookie',
                        options= [{'label': player, 'value': player} for player in dfrookie["player"]],
                        value= dfrookie["player"].iloc[0]
                )),
    dash_table.DataTable(
        id='player-table-rookie',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        fixed_rows={'headers': True},
        style_table={'overflowX': 'auto'}
        ),
    html.Button(dcc.Link("Revenir à la page d'accueil", href='/'))
],style =  {'background' : 'beige','width': '50%', 'float': 'left'} )

@app.callback(
    Output('player-table-rookie',"data"),
    [Input("player-Dropdown-rookie","value")]
)

def update_table(player_name):
    player_info = df[df['player'] == player_name]
    return player_info.to_dict("records")


# Div Senior
dfsenior = dfnba[dfnba["age"]>=24]
div_senior = html.Div([
    html.H1('Senior', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Div(dcc.Dropdown(id = 'player-Dropdown',
                        options= [{'label': player, 'value': player} for player in dfsenior["player"]],
                        value= dfsenior["player"].iloc[0]
                )),
    html.Div(id='output-div'),
    html.Button(dcc.Link("Revenir à la page d'accueil", href='/'))
],style = {'background' : 'beige','width': '50%', 'float': 'left'}  )

@app.callback(
    Output('output-div',"children"),
    [Input("player-Dropdown","value")]
)

def update_output(player_name):
    player_info = df[df['player'] == player_name]
    return html.Div([
        html.H3(f'Player: {player_info["player"].values[0]}'),
        html.P(f'position: {player_info["pos"].values[0]}'),
        html.P(f'age: {player_info["age"].values[0]}'),
        html.P(f'team ID: {player_info["bref_team_id"].values[0]}'),
        html.P(f'Minute joué: {player_info["mp"].values[0]}'),
        html.P(f'Minute joué: {player_info["mp"].values[0]}'),
        
    ])


# set 2 div together
layout_1 = html.Div(children=[div_rookie,div_senior])



#################################################################



# page2 selectionner de seniors

#TODO get position list (df)
dfposition = dfnba["pos"].unique().tolist()

#TODO: get list of caractere, the list of titles columne
columns = df.columns.tolist()
#TODO drop player name, team name 
character = [c for c in columns if c not in ["player","bref_team_id","season","age","pos"]]

dfteam = dfnba["bref_team_id"].to_frame()

########################################################################
#Team1
Div_Team1 = html.Div([
dcc.Dropdown(id = 'Team_Dropdown1',
                        options= [{'label': title, 'value': title} for title in character],
                        value= character[0]
                ),
 
dcc.Graph(id='bar-chart-1'),


],style = {'background' : 'beige','width': '30%', 'float': 'left'}  )

# connect Team_Dropdown1 and bar-chart-1
@app.callback(
    Output('bar-chart-1', 'figure'),
    [Input('Team_Dropdown1', 'value')]
)
def update_chart(selected_column):
    #TODO use aggraage calcule "ex. nombre de passes." ascending
    agg_df = df.groupby('bref_team_id')[selected_column].sum().sort_values(ascending=True)
    # got top 5 team according to dropdown selected

    top_5_teams = agg_df.head(5)
    
    # 
    bar_chart = go.Bar(x=top_5_teams.values, y=top_5_teams.index,orientation='h')
    return {'data': [bar_chart], 'layout': go.Layout(title=f'Total {selected_column} by Team ID')}



#####################################################################################################
#Team2
# Div_Team2 = html.Div([
# dcc.Dropdown(id = 'Team_Dropdown1',
#                         options= [{'label': team, 'value': team} for team in dfteam["bref_team_id"]],
#                         value= dfteam["bref_team_id"].iloc[0]
#                 )
# ],style = {'background' : 'beige','width': '50%', 'float': 'left'}  )

################################################################
#Postion 
Div_position = html.Div([
html.Div(dcc.Slider(id = 'slider_1',
                      min = 0,
                      max = len(dfposition)-1,
                      marks={i:dfposition[i] for i in range(len(dfposition))},
                      step = 1)),
dcc.Graph(id="bar_position")
],style = {'background' : 'beige','width': '30%', 'float': 'right'})

@app.callback(
    Output("bar_position","figure"),
    [Input("slider_1","value")]
)
def update_chart_position(position_selected):
    #TODO use aggraage calcule posotion ascending
    postion_df = df.groupby('pos')[position_selected].sum().sort_values(ascending=True)
    top_5_postion = postion_df.head(5)

    bar_chart = go.Bar(x=top_5_postion.value,y=top_5_postion.index,orientation="h")
    return {
        "data":[bar_chart],
        "layout":go.layout(title = f'Top 5 team have {position_selected} postion')
    }

####################################################################
#layout2 together
layout_2 = html.Div([
    html.Div(children=[Div_Team1,Div_position]), #Div_Team2
    html.Button(dcc.Link("Revenir à la page d'accueil", href='/'))
])


# Mise à jour de l'index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return layout_1
    elif pathname == '/page-2':
        return layout_2
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')