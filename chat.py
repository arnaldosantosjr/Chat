
import flet as ft

def main(page: ft.Page):
    page.title = "WebChat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # Área onde as mensagens serão exibidas
    chat = ft.Column()
    
    nome_usuario = ft.TextField(label="Seu nome")

    campo_mensagem = ft.TextField(label="Digite sua mensagem", expand=True)

    def enviar_mensagem(e):
        if nome_usuario.value and campo_mensagem.value:
            nova_mensagem = ft.Text(f"{nome_usuario.value}: {campo_mensagem.value}")
            chat.controls.append(nova_mensagem)
            campo_mensagem.value = ""
            page.update()

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(e):
        if not nome_usuario.value:
            page.dialog = ft.AlertDialog(title=ft.Text("Por favor, digite seu nome"))
            page.dialog.open = True
            page.update()
            return

        page.clean()  # limpa a tela
        page.add(
            ft.Text(f"Bem-vindo ao WebChat, {nome_usuario.value}!", size=20),
            chat,
            ft.Row([campo_mensagem, botao_enviar])
        )

    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    page.add(
        ft.Text("WebChat", size=30, weight="bold"),
        nome_usuario,
        botao_entrar
    )

# Rodar no navegador
ft.app(target=main, view=ft.WEB_BROWSER)
