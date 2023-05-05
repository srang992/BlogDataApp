import webbrowser
import flet as ft
import pyperclip


def ArticleCard(page, title, author, link):

    async def open_link(e):
        await page.launch_url_async(link)

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
