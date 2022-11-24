# LinuxResourceDashboard
 A dashboard to monitor Linux resource usage

## Instalação venv
Passo a passo para instalar e ativar ambiente virtual python.
```bash
python3 apt install python3.8-venv

py -m venv virt
source virt/bin/activate
```

### Se estiver programando para Linux no Windows com VSCode
É necessário WSL instalado.

Passo a passo em https://code.visualstudio.com/docs/remote/wsl

No VSCode, instale o pack de extensões Remote Development (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Depois, no terminal do Linux (WSL), navegue até a pasta do projeto. Abra o VSCode com o comando 
```bash
code .
```
Depois, o interpretador do venv deve estar disponível. Também pode ser configurado via "Python: select interpreter" no  
command palette.

## Instalando o Kivy
Instruções detalhadas podem ser encontradas em https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip

```bash
python3 -m pip install "kivy[base]" kivy_examples
```
>"This also installs the minimum dependencies of Kivy. To additionally install Kivy with audio/video support, install either kivy[base,media] or kivy[full]. See Kivy’s dependencies for the list of selectors."

## Playlists úteis
### Python GUI's With Kivy
by Codemy.com

https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg

### Ecommerce Dashboard UI
by Samuel Mthembo

https://youtube.com/playlist?list=PLRUcPloZy-I_OLpvphqnz5zaqKRHncoZ6


## Utils
```bash
alias py=python3
```