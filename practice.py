# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 08:05:50 2022

@author: ELCOT
"""
import dash
from flask import Flask
import pandas as pd # creating and manipulating dataframes
import plotly.graph_objects as go # we can not use express plots
from plotly.subplots import make_subplots # creating subplots

# df = sns.load_dataset('tips')
# grouped_df = df.groupby(['sex', 'day'], as_index=False).sum()
# grouped_df.head()


app = dash.Dash(__name__)
df = pd.read_csv("vgsales.csv")

# df = pd.DataFrame({'world_rank': [1, 2, 3, 4, 5],
                    # 'university_name': ['Harvard', 'MIT', 'Stanford', 'Cambridge', 'Oxford'],
                    # 'citations': [80, 70, 60, 50, 40]})

# print(grouped_df)

# print(df)
# @app.route("/")
# def home():

fig = make_subplots(rows=2, cols=2,specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "domain"}, {"type": "domain"}]],subplot_titles=('Teams&Members','Productivity','sales/month','Best Team'))
    
# # add the 1st graph by specifying which row and column it will come to
fig.add_trace(go.Bar(x=df['Teams'], y=df['Members'],name='Members/team'),row=1, col=1)
# # add the 2nd graph
fig.add_trace(go.Scatter(x=df['Teams'], y=df['Productivity'],name='Productivity/Team'), row=1, col=2)

fig.add_trace(go.Pie(values=df['Total_Sales'],labels=df['Teams']),row=2, col=1)

fig.add_trace(go.Pie(values=df['Productivity'],labels=df['Teams'],pull=[0, 0, 0.2, 0,0,0,0,0,0,0]),row=2, col=2)
    

fig.show()

#     # figure=fig.show()
# return fig
    

if __name__ == '__main__':
   app.run_server(debug=True)



# -----------------------------------------------------------------------------

# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import pandas as pd

# df = pd.DataFrame({'world_rank': [1, 2, 3, 4, 5],
#                     'university_name': ['Harvard', 'MIT', 'Stanford', 'Cambridge', 'Oxford'],
#                     'citations': [98.8, 98.7, 97.6, 97.5, 96]})

# layout = dict(plot_bgcolor='white',
#               margin=dict(t=20, l=20, r=20, b=20),
#               xaxis=dict(title='World Rank',
#                           range=[0.9, 5.5],
#                           linecolor='#d9d9d9',
#                           showgrid=False,
#                           mirror=True),
#               yaxis=dict(title='Citations',
#                           range=[95.5, 99.5],
#                           linecolor='#d9d9d9',
#                           showgrid=False,
#                           mirror=True))

# data = go.Scatter(x=df['world_rank'],
#                   y=df['citations'],
#                   text=df['university_name'],
#                   textposition='top right',
#                   textfont=dict(color='#E58606'),
#                   mode='lines+markers+text',
#                   marker=dict(color='#5D69B1', size=8),
#                   line=dict(color='#52BCA3', width=1, dash='dash'),
#                   name='citations')

# fig = go.Figure(data=data, layout=layout)

# fig.show()

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

# fig = make_subplots(
#     rows=2, cols=2,
#     specs=[[{"type": "bar"}, {"type": "barpolar"}],
#             [{"type": "pie"}, {"type": "scatter3d"}]],
# )

# fig.add_trace(go.Bar(y=[2, 3, 1]),
#               row=1, col=1)

# fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
#               row=1, col=2)

# fig.add_trace(go.Pie(values=[2, 3, 1]),
#               row=2, col=1)

# fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
#                             z=[0.5, 1, 2], mode="lines"),
#               row=2, col=2)

# fig.update_layout(height=700, showlegend=False)

# fig.show()




# import dash
# import plotly.express as px
# import pandas as pd
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Output, Input
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

# df = pd.read_csv("vgsales.csv")

# fig = make_subplots(rows=1, cols=2)

# fig.add_trace(go.pie(data_frame=df, names='Genre', values='Japan Sales')row=1,col=1)
# fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
# fig.show()
# fig_pie1 = px.pie(data_frame=df, names='Genre', values='North American Sales')
# fig_pie.show()
# fig_pie1.show()

# app = dash.Dash(__name__)

# app.layout=html.Div([
#     html.H1("Graph Analysis with Charming Data"),
#     dcc.Dropdown(id='genre-choice',
#                  options=[{'label':x, 'value':x}
#                           for x in sorted(df.Genre.unique())],
#                  value='Action',
#                  style={'width':'50%'}
#                  ),
#     dcc.Dropdown(id='platform-choice',
#                  options=[{'label': x, 'value': x}
#                           for x in sorted(df.Platform.unique())],
#                  value='PS4',
#                  style={'width':'50%'}
#                  ),
#     dcc.Graph(id='my-graph',
#               figure={}),
# ])
# @app.callback(
#     Output(component_id='my-graph', component_property='figure'),
#     Input(component_id='genre-choice', component_property='value'),
#     Input(component_id='platform-choice', component_property='value')
# )
# def interactive_graphs(value_genre, value_platform):
#     dff = df[df.Genre==value_genre]
#     dff = dff[dff.Platform==value_platform]
#     fig = px.bar(data_frame=dff, x='Year', y='Japan Sales')
#     return fig


# if __name__=='__main__':
#     app.run_server()
