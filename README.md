# LinuxResourceDashboard
 A dashboard to monitor the of the resources of a Linux System.

 [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
 [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)

> **Note**: <br/>Para informações detalhadas, consulte o arquivo do relatório final: [LinuxResourcesDashboard.pdf](LinuxResourcesDashboard.pdf) 


## Setup do projeto
É necessário ter instalado o Python 3.
No terminal, installe o Dash e o Plotly:
```bash
pip install dash
pip install plotly==5.11.0
```



#### Se estiver programando para Linux no Windows com VSCode
É necessário WSL instalado.

Passo a passo em https://code.visualstudio.com/docs/remote/wsl

No VSCode, instale o pack de extensões Remote Development (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Depois, no terminal do Linux (WSL), navegue até a pasta do projeto. Abra o VSCode com o comando 
```bash
code .
```
## Execução

Após clonar o repositório do github, acessar o diretório "dashApp"e executar o arquivo "dashboard.py"usando Python 3:

```bash
cd dashApp
python3 dashboard.py
```

No navegador de sua preferência (Google Chrome é recomendado), acesse o endereço "http://127.0.0.1:8050/".

Caso encontre problemas ao ao encerrar ou reiniciar o dashboard relacionados à porta 8050 que não foi fechado execute o comando

```bash
lsof -i:8050 | grep python3
```

E encerre o processo cujo PID é o primeiro da lista retornada pelo comando anterior. Por exem-
plo, supondo que a saída seja:

```bash
python3 11970 gabriel    4u  IPv4 1274422      0t0  TCP localhost:8050 (LISTEN)
python3 11970 gabriel    6u  IPv4 1274422      0t0  TCP localhost:8050 (LISTEN)
python3 12042 gabriel    4u  IPv4 1274422      0t0  TCP localhost:8050 (LISTEN)
python3 12042 gabriel    6u  IPv4 1274422      0t0  TCP localhost:8050 (LISTEN)
```

Execute

```bash
kill -9 11970
```

## Interface

![Tela inicial](/assets/designReference/dashboard.jpg)

Ao abrir o dashboard, vê-se a tela da figura acima. A interface tem áreas para CPU, memória,
discos, informações do sistema e processos. Mais abaixo, rolando a tela, há um terminal, como
mostra a figura seguinte.

![Tela inicial](/assets/designReference/dashboard-terminal.jpg)

> **IMPORTANTE:** para informações detalhadas, consulte o arquivo [LinuxResourcesDashboard.pdf](LinuxResourcesDashboard.pdf) 

## Playlists úteis
#### Python GUI's With Kivy
by Codemy.com

https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg

#### Ecommerce Dashboard UI
by Samuel Mthembo

https://youtube.com/playlist?list=PLRUcPloZy-I_OLpvphqnz5zaqKRHncoZ6

#### Python GUI's With TKinter
by Codemy

https://youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV


### Outros dashboards linux
https://afaqurk.github.io/linux-dash/#/system-status




### Utils
```bash
alias py=python3
```
#### Configure ABNT2 keyboard on WSL GUI apps

first step, configure your locale

```bash
sudo dpkg-reconfigure locales
```

on the screen scroll down and choose pt_BR.UTF8. 
then next you will do ok and ok, and run this on the command line

```bash
sudo update-locale LANG=pt_BR.UTF8
```

in the end you run this

```bash
setxkbmap -model abnt2 -layout br -variant abnt2
```

Mais detalhes em https://github.com/microsoft/wslg/issues/27

#### Shell commands in Python

https://janakiev.com/blog/python-shell-commands/



## Interface antiga

### Layout da tela principal

![Layout da tela principal](/assets/designReference/MainScreen.jpg)

Interface antiga (Tkinter):

![Interface da tela principal](/assets/designReference/screenshoot-v0.jpg)


