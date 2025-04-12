# sites / Sistemas / Aplicativos
# Flask
# Django
# FastAPI
# Flet -> Python -> visal (frontand) / logica (backend)
# Kivy

# Frameworks -> biblioteca com regras especificas

# Criar o chat

# Títulho: WebChat
# Cotão: Iniciar Chat no botão
    # Quando clicar no botão:
    # - Criar uma nova janela/Dialog/Modal
        # Título: Bem-vindo ao WebChat
        # Campo de texto: Escreva seu nome no chat
        # Botão: Enviar
            #Clcou no botão:
            # Fechar a janela/Dialog/Modal
                # Criar  o chat
                # Criar o campo de texto para o chat: Digite sua mensagem
                # Botão: Enviar
                    # Quando clicar no botão:
                    # Enviar a mensagem para o chat


#importando o flet
import flet as ft


# Criando a função principal
def main(page):
    #Crianddo elementos
    title = ft.Text("Webchat")

    #Criando o botão
    def abrir_dialogo(evento):
        print("Botão clicado")
    botton_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialogo)

    #Colocando os elementos na tela
    page.add(title)
    page.add(botton_iniciar)

# Rodandar o aplicativo
ft.app(main)