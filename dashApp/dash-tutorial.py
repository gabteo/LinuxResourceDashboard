import dash
import pandas as pd
from dash import dcc, html, Input, Output, State, dash_table
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
    html.Div(children=[
      html.Div(
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
            html.Div(children=["Discos"], className="card-title"),
            dcc.Graph(
            id="discos-inicio-chart",
            #config={"displayModeBar": False},
            )
          ],
          className="card card-menor",
        ),
        #labels
        html.Div(
          children= [
            html.Div(children= [
              html.Div(children=["Uso (%)"], className="card-mini-title"),
              html.Div(children=[""], id="label-cpu-usado", className="card-mini-content")
            ], className="card card-mini-cpu"),
          ],
          className="card card-menor",
        ),
        html.Div(
          children= [
            html.Div(children= [
              html.Div(children=["Mem. Total (kB)"], className="card-mini-title"),
              html.Div(children=[""], id="label-mem-tot", className="card-mini-content")
            ], className="card card-mini-mem"),
            html.Div(children= [
              html.Div(children=["Mem. Usada (kB)"], className="card-mini-title"),
              html.Div(children=[""], id="label-mem-usd", className="card-mini-content")
            ], className="card card-mini-mem"),
            html.Div(children= [
              html.Div(children=["Swap total (kB)"], className="card-mini-title"),
              html.Div(children=[""], id="label-swp-tot", className="card-mini-content")
            ], className="card card-mini-mem"),
            html.Div(children= [
              html.Div(children=["Swap Usada (kB)"], className="card-mini-title"),
              html.Div(children=[""], id="label-swp-usd", className="card-mini-content")
            ], className="card card-mini-mem"),
          ],
          className="card card-menor",
        ),
        html.Div(
          children= [
            html.Div(children= [
              html.Div(children=["Disco 1 (kB)"], className="card-mini-title"),
              html.Div(children=["1"], id="label-disc1-usd", className="card-mini-content")
            ], className="card card-mini-disc"),
            html.Div(children= [
              html.Div(children=["Disco 2 (kB)"], className="card-mini-title"),
              html.Div(children=["2"], id="label-disc2-usd", className="card-mini-content")
            ], className="card card-mini-disc"),
            html.Div(children= [
              html.Div(children=["Disco 3 (kB)"], className="card-mini-title"),
              html.Div(children=["3"], id="label-disc3-usd", className="card-mini-content")
            ], className="card card-mini-disc"),
          ],
          className="card card-menor",
        ),
        html.Div(
          children= [
            html.Div(children=["Sistema"], className="card-title"),
            html.Div(children= [
              html.Div(children=["Processador"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getModelNamet()}"], className="card-mini-content")
            ], className="card card-mini-info-proc"),
            html.Div(children= [
              html.Div(children=["Arquitetura"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getArchitecture()}"], className="card-mini-content")
            ], className="card card-mini-info"),
            html.Div(children= [
              html.Div(children=["Frequência (MHz)"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getCpuMhz()}"], className="card-mini-content")
            ], className="card card-mini-info"),
            html.Div(children= [
              html.Div(children=["Cores"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getNumberOfCores()}"], className="card-mini-content")
            ], className="card card-mini-info"),
            html.Div(children= [
              html.Div(children=["Cores por socket"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getCoresPerSocket()}"], className="card-mini-content")
            ], className="card card-mini-info"),
            html.Div(children= [
              html.Div(children=["Threads por core"], className="card-mini-title"),
              html.Div(children=[f"{data.cpuData.getThreadsPerCore()}"], className="card-mini-content")
            ], className="card card-mini-info"),
            
          ],
          className="card card-info",
        ),
        #processos
        html.Div(
          children= [
            html.Div(children=["Processos"], className="card-title"),
            html.Div(children=[
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
            ])
            
          ],
          className="card card-table",
        ),
        #terminal
        html.Div(
          children= [
            html.Div(children=["Terminal"], className="card-title"),
            html.Div(children=[
              dcc.Input(id='comando', placeholder='Digite o comando', type='text', className="input-comando"),
              html.Button(id='submit-button', type='submit', children='Rodar comando', className="btn-comando"),
              html.Div(id='output_div')
            ], className="card-terminal-content")
          ],
          className="card card-table",
        ),
        
      ]
    )
    ],id='tabs-content', className="wrapper"),
    dcc.Interval(
      id='interval-component',
      interval=1*1000,
      n_intervals = 0
    )
  ])

# @app.callback(Output('tabs-content', 'children'),
#               Input('tabs', 'value'))
# def render_content(tab):
#   if tab == 'inicio':
#     return 

listaCPUx = list(range(60))
listaCPUy = [0]*60

listaMEMx = list(range(60))
listaMEMy = [0]*60

listaSWAPy = [0]*60

@app.callback(Output('cpu-inicio-chart', 'figure'), Output('memoria-inicio-chart', 'figure'), Output('discos-inicio-chart', 'figure'), Output('tbl_processos', 'data'),
  Output('label-cpu-usado','children' ), Output('label-mem-tot','children' ), Output('label-mem-usd','children' ),
  Output('label-swp-tot','children' ), Output('label-swp-usd','children' ), Input('interval-component', 'n_intervals'))

def update_inicio(n) :

  listaCPUy.pop(0)
  cpuUsado = data.cpuData.getTotalUsage()
  listaCPUy.append(cpuUsado)

  cpu_chart_figure = {
    "data": [
      {
        'x': listaCPUx, 
        'y' : listaCPUy, 
        'type': 'line', 
        'name':'uso',
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

  memTotal = dictMEM["MemTotal"]
  memUsado = (dictMEM["MemTotal"] - dictMEM["MemFree"])

  swpTotal = dictMEM["SwapTotal"]
  swpUsado = (dictMEM["SwapTotal"] - dictMEM["SwapFree"])

  listaMEMy.append(memUsado * 100/memTotal)

  listaSWAPy.pop(0)
  listaSWAPy.append(swpUsado * 100/swpTotal)


  memoria_chart_figure = {
    "data": [
      {
        'x': listaMEMx, 
        'y' : listaMEMy, 
        'type': 'line', 
        'name':'memoria',
        'fill':'tozeroy'
      },
      {
        'x': listaMEMx, 
        'y' : listaSWAPy, 
        'type': 'line', 
        'name':'swap',
        'fill':'tozeroy'
      }
    ],
    "layout": {
      "yaxis" : {"fixedrange":True, "range": [0,100]},
      "xaxis" : {"fixedrange":True ,"visible": False}
    }
  }

  discos_chart_figure = {
    "data": [
      {
        #dados da parte livre de cada disco
        'orientation': 'h',
        'type': 'bar', 
        'name':'usado',
        'x': [140, 120, 100], 
        'y':['disco 1', 'disco 2', 'disco 3']
        
      },
      {
        #dados da parte usada de cada disco
        'orientation': 'h',
        'type': 'bar', 
        'name':'livre',
        'x': [140, 160, 180], 
        'y':['disco 1', 'disco 2', 'disco 3']
      }
    ],
    "layout": {
      "yaxis" : {"showgrid":False, 
                 "showline": False, 
                "showticklabels": True,
                "zeroline": False,
                "visible" : True
                },
      "xaxis" : {"showgrid":False, 
                 "showline": False, 
                 "showticklabels": False,
                 "zeroline": False,
                 "visible" : True
                },
      "barmode": "stack"
    }
  }

  _,data_pd = data.processesData.getProcesses()

  df_processo = pd.DataFrame.from_dict(data_pd)
  
  return cpu_chart_figure, memoria_chart_figure, discos_chart_figure, df_processo.to_dict('records'), cpuUsado, memTotal, memUsado, swpTotal, swpUsado

@app.callback(Output('output_div', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('comando', 'value')],
                  )
def update_output(clicks, input_value):
        if clicks is not None:
            return execCmd(input_value)

def execCmd(cmd: str) -> str:
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()

if __name__ == '__main__':
  #cmd = "lsof -i:8050 | grep python3 | awk '{print $2}' | awk 'FNR == 0 { print }'"
  #pid = execCmd(cmd)
  #execCmd("kill -9 {pid}")
  app.run_server(debug=True)
  
#cat <( </dev/zero head -c 500m) <(sleep 1) | tail