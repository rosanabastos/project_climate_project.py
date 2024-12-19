import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Importando Pillow para carregar e exibir a imagem
import requests  # Biblioteca para fazer requisições HTTP

############## cores #############
co0 = "#444466"  # Preta 
Co1 = "#feffff"  # Branca 
Co2 = "#6f9fbd"  # Vermelho 

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia  # Escolha o fundo

# Criação da janela
janela = Tk()
janela.title('Clima em Tempo Real')
janela.geometry('320x350')
janela.configure(bg=fundo)

# Separator horizontal
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# criando frames
frame_top = Frame(janela, width=320, height=50, bg=Co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Função para buscar o clima
def buscar_clima():
    cidade = e_local.get()  # Obtém a cidade inserida no campo de texto
    if cidade:
        try:
            # Substitua pela sua API Key do OpenWeatherMap
            API_KEY = "62d221be997254ec27e01ea10253cbf5"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
            resposta = requests.get(url)
            dados = resposta.json()
            
            if resposta.status_code == 200:
                # Atualiza os dados na interface
                l_cidade.config(text=f"{dados['name']} - {dados['sys']['country']}")
                l_data.config(text=f"Temperatura: {dados['main']['temp']}°C")
                l_umidade.config(text=f"{dados['main']['humidity']}%")
                l_u_nome.config(text=f"Umidade do ar {dados['main']['humidity']}%")
                l_pressao.config(text=f"Condição: {dados['weather'][0]['description']}")
                l_descricao.config(text=f"Pressão: {dados['main']['pressure']} hPa")
            else:
                l_cidade.config(text="Cidade não encontrada!")
        except Exception as e:
            l_cidade.config(text="Erro ao buscar dados!")
    else:
        l_cidade.config(text="Insira uma cidade!")

# Configurando frame top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_ver = Button(frame_top, text='Clima', bg=Co1, fg=Co2, font=("Ivy 7 bold",), relief='raised', overrelief=RIDGE, command=buscar_clima)
b_ver.place(x=250, y=10)

# Configurando frame corpo
l_cidade = Label(frame_corpo, text='Insira uma cidade e clique em Clima', anchor="center", bg=fundo, fg=Co1, font=("Arial 14",))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor="center", bg=fundo, fg=Co1, font=("Arial 10",))
l_data.place(x=10, y=54)

l_umidade = Label(frame_corpo, text='', anchor="center", bg=fundo, fg=Co1, font=("Arial 45"))
l_umidade.place(x=10, y=80)

l_u_nome = Label(frame_corpo, text='', anchor="center", bg=fundo, fg=Co1, font=("Arial 8"))
l_u_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='', anchor="center", bg=fundo, fg=Co1, font=("Arial 10",))
l_pressao.place(x=10, y=184)

l_descricao = Label(frame_corpo, text='', anchor="center", bg=fundo, fg=Co1, font=("Arial 10",))
l_descricao.place(x=10, y=212)

# Chama o loop principal da interface gráfica
janela.mainloop()





