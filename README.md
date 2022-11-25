# LinuxResourceDashboard
 A dashboard to monitor Linux resource usage

## Setup do projeto

### Instalação venv
Passo a passo para instalar e ativar ambiente virtual python.
```bash
python3 apt install python3.8-venv

py -m venv virt
source virt/bin/activate
```

#### Se estiver programando para Linux no Windows com VSCode
É necessário WSL instalado.

Passo a passo em https://code.visualstudio.com/docs/remote/wsl

No VSCode, instale o pack de extensões Remote Development (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Depois, no terminal do Linux (WSL), navegue até a pasta do projeto. Abra o VSCode com o comando 
```bash
code .
```
Depois, o interpretador do venv deve estar disponível. Também pode ser configurado via "Python: select interpreter" no  
command palette.

### Instalando Tkinter
```bash
pip install tk
```

Se não funcionar, 
```bash
sudo apt-get install python3-tk
```

#### Instalando CustomTkinter UI-Library

Biblioteca com interface mais bonita para tkinter.

Documentação disponível em https://github.com/TomSchimansky/CustomTkinter

```bash
pip3 install customtkinter
```

### Instalando o Kivy
Instruções detalhadas podem ser encontradas em https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip

```bash
python3 -m pip install "kivy[base]" kivy_examples
```
>"This also installs the minimum dependencies of Kivy. To additionally install Kivy with audio/video support, install either kivy[base,media] or kivy[full]. See Kivy’s dependencies for the list of selectors."

### Playlists úteis
#### Python GUI's With Kivy
by Codemy.com

https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg

#### Ecommerce Dashboard UI
by Samuel Mthembo

https://youtube.com/playlist?list=PLRUcPloZy-I_OLpvphqnz5zaqKRHncoZ6


### outras dashboards linux
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

## Design

### Layout da tela principal

![Layout da tela principal](/assets/designReference/MainScreen.jpg)

