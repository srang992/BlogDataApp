import os
import flet as ft
import pyperclip


def ArticleCard(title, author, link):

    def open_link(e):
        if os.name =='nt':
            os.system('start ' + link)
        else:
            os.system('xdg-open ' + link)

    def copy_link(e):
        pyperclip.copy(link)

    return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ARTICLE),
                            title=ft.Text(title, color="black"),
                            subtitle=ft.Text(author),
                            disabled=True,
                        ),
                        ft.Row(
                            [ft.TextButton("Go to Link", icon="link", on_click=open_link)],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
