import dash
import pandas as pd
from dash import dcc, html, Input, Output, dash_table
from database import database
from systemData import *

db = database()
data = systemData(db)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
  children=[
    html.Div(
      children=[
        html.Div(
          children=[
            html.Img(src="assets/linux.png", className="logo-img"),
            html.H1(
              children = "Linux Resources Dashboard", className = "header-title"
            ),
            html.P(children="Desenvolvido por Gabriel Hrysay e Misael Costa", className="header-description")
          ],
          className = "header-container-title"
        ),
        
      ],
      className="header"
    ),
    dcc.Tabs(id="tabs", value="inicio", children=[
      dcc.Tab(label='Início', value='inicio', className='custom-tab', selected_className = 'custom-tab-selected'),
      #dcc.Tab(label='CPU', value='cpu', className='custom-tab', selected_className = 'custom-tab-selected'),
      #dcc.Tab(label='Memória', value='memoria', className='custom-tab', selected_className = 'custom-tab-selected'),
      #dcc.Tab(label='Informações', value='info', className='custom-tab', selected_className = 'custom-tab-selected'),
      dcc.Tab(label='Terminal', value='terminal', className='custom-tab', selected_className = 'custom-tab-selected'),
    ]),
    html.Div(id='tabs-content', className="wrapper"),
    dcc.Interval(
      id='interval-component',
      interval=1*1000,
      n_intervals = 0
    )
  ])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
  if tab == 'inicio':
    return html.Div(
      children = [
        html.Div(
          children= [
            html.Div(children=["CPU"], className="card-title"),
            
            dcc.Graph(
            id="cpu-inicio-chart",
            config={"displayModeBar": False},
            )
          ],
          className="card card-menor",
        ),
        html.Div(
          children= [
            html.Div(children=["Memória"], className="card-title"),
            dcc.Graph(
            id="memoria-inicio-chart",
            config={"displayModeBar": False},
            )
          ],
          className="card card-menor",
        ),
        html.Div(
          children= [
            html.Div(children=["Processos"], className="card-title"),
            dash_table.DataTable(
              id="tbl_processos", 
              columns=[
                {'name': 'PID', 'id': 'PID'}, 
                {'name': 'USER', 'id': 'USER'}, 
                {'name': 'STATUS', 'id': 'STATUS'},
                {'name': 'CPU', 'id': 'CPU'}, 
                {'name': 'MEM', 'id': 'MEM'}
              ],
              filter_action="native",
              sort_action="native",
              sort_mode="multi",
              )
            # html.Table([
            #   html.Thead([
            #     html.Tr([
            #       html.Th('Nome', style = {"width": "50%"}),
            #       html.Th('Status'),
            #       html.Th('CPU'),
            #       html.Th('Memória'),
            #     ]),
            #   ]),
            #   html.Tbody([
            #     html.Tr([
            #       html.Td('teste'),
            #       html.Td('teste'),
            #       html.Td('teste'),
            #       html.Td('teste'),
            #     ]),
            #   ])
            # ])
          ],
          className="card card-table",
        ),
        html.Div(
          children= [
            html.Div(children=["Sistema"], className="card-title"),
            f"{data.cpuData.getModelNamet()} | Número de Cores: {data.cpuData.getNumberOfCores()} | Cores por socket: {data.cpuData.getCoresPerSocket()} | "
          ],
          className="card card-info",
        ),
      ]
    )
  elif tab == 'cpu':
    return html.Div(children = [
      "teste",
        dcc.Graph(id='example', 
        figure = {
          'data': [
            {
              'x': [1,2,3], 
              'y' : [5,6,7], 
              'type': 'line', 
              'name':'memory',
              'fill':'tozeroy'
            }
          ]
        })

    ])
  elif tab == 'memoria':
    return html.Div([

    ])
  elif tab == 'info':
    return html.Div([

    ])
  elif tab == 'terminal':
    return html.Div([

    ])

listaCPUx = list(range(60))
listaCPUy = [0]*60

listaMEMx = list(range(60))
listaMEMy = [0]*60

@app.callback(Output('cpu-inicio-chart', 'figure'), Output('memoria-inicio-chart', 'figure'), Output('tbl_processos', 'data'),
  Input('interval-component', 'n_intervals'))

def update_inicio(n) :

  listaCPUy.pop(0)
  listaCPUy.append(data.cpuData.getTotalUsage())

  cpu_chart_figure = {
    "data": [
      {
        'x': listaCPUx, 
        'y' : listaCPUy, 
        'type': 'line', 
        'name':'memory',
        'fill':'tozeroy'
      }
    ],
    "layout": {
      "yaxis" : {"fixedrange":True, "range": [0,100]},
      "xaxis" : {"fixedrange":True ,"visible": False}
    }
  }

  _,dictMEM = data.memoryData.getMemStats();
  listaMEMy.pop(0)

  listaMEMy.append((dictMEM["MemTotal"] - dictMEM["MemFree"]) * 100/dictMEM["MemTotal"])

  memoria_chart_figure = {
    "data": [
      {
        'x': listaMEMx, 
        'y' : listaMEMy, 
        'type': 'line', 
        'name':'memory',
        'fill':'tozeroy'
      }
    ],
    "layout": {
      "yaxis" : {"fixedrange":True, "range": [0,100]},
      "xaxis" : {"fixedrange":True ,"visible": False}
    }
  }

  _,data_pd = data.processesData.getProcesses()

  df_processo = pd.DataFrame.from_dict(data_pd)
  
  return cpu_chart_figure, memoria_chart_figure, df_processo.to_dict('records')

def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()

if __name__ == '__main__':
  #cmd = "lsof -i:8050 | grep python3 | awk '{print $2}' | awk 'FNR == 0 { print }'"
  #pid = execCmd(cmd)
  #execCmd("kill -9 {pid}")
  app.run_server(debug=True)
  
#cat <( </dev/zero head -c 500m) <(sleep 1) | tail