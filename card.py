import flet as ft


def ArticleCard(page, title, desc, link):

    async def open_link(e):
        await page.launch_url_async(link)

    return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ARTICLE),
                            title=ft.Text(title,
                                          style=ft.TextThemeStyle.TITLE_SMALL,
                                          size=16,
                                          max_lines=2,
                                          overflow=ft.TextOverflow.ELLIPSIS),
                            subtitle=ft.Text(desc, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            disabled=True,
                        ),
                        ft.Row(
                            [ft.TextButton("Go to Link", icon="link", on_click=open_link)],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                ),
                width=400,
                padding=10,
            )
        )
