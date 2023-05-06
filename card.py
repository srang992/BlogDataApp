import flet as ft


def ArticleCard(page, title, desc, link):
    async def open_link(e):
        await page.launch_url_async(link)

    async def copy_link(e):
        await page.set_clipboard_async(link)
        await page.show_snack_bar_async(
            ft.SnackBar(ft.Text("Link copied to clipboard"), open=True)
        )

    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE),
                        title=ft.Text(title,
                                      style=ft.TextThemeStyle.TITLE_SMALL,
                                      size=18,
                                      max_lines=2,
                                      font_family="Courgette",
                                      overflow=ft.TextOverflow.ELLIPSIS),
                        subtitle=ft.Text(desc, max_lines=2, font_family="Alkatra", overflow=ft.TextOverflow.ELLIPSIS),
                        disabled=True,
                    ),
                    ft.Row(
                        [ft.TextButton(
                            content=ft.Row([
                                ft.Icon(ft.icons.COPY),
                                ft.Text("Copy Link", font_family="Courgette")
                            ]),
                            on_click=copy_link),
                            ft.TextButton(
                                content=ft.Row([
                                    ft.Icon(ft.icons.LINK),
                                    ft.Text("Open Link", font_family="Courgette")
                                ]),
                                on_click=open_link,)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
        )
    )
