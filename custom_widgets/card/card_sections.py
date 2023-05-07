import flet as ft


class CardDetails(ft.UserControl):
    def __init__(self, title: str, desc: str,
                 title_font_family: str = None,
                 subtitle_font_family: str = None):
        super().__init__()
        self.title = title
        self.desc = desc
        self.title_font_family = title_font_family
        self.subtitle_font_family = subtitle_font_family

    def build(self):
        return ft.ListTile(
            leading=ft.Icon(ft.icons.ARTICLE),
            title=ft.Text(self.title,
                          style=ft.TextThemeStyle.TITLE_SMALL,
                          size=18,
                          max_lines=2,
                          font_family=self.title_font_family,
                          overflow=ft.TextOverflow.ELLIPSIS),
            subtitle=ft.Text(self.desc, max_lines=2, font_family=self.subtitle_font_family,
                             overflow=ft.TextOverflow.ELLIPSIS),
            disabled=True,
        )


class CardButtons(ft.UserControl):
    def __init__(self, link: str, font_family: str = None):
        super().__init__()
        self.link = link
        self.font_family = font_family

    def build(self):
        async def open_link(e):
            await self.page.launch_url_async(self.link)

        async def copy_link(e):
            await self.page.set_clipboard_async(self.link)
            await self.page.show_snack_bar_async(
                ft.SnackBar(ft.Text("Link copied to clipboard"), open=True)
            )

        return ft.Row(
            [
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.COPY),
                        ft.Text("Copy Link", font_family=self.font_family)
                    ]),
                    on_click=copy_link, ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.LINK),
                        ft.Text("Open Link", font_family=self.font_family)
                    ]),
                    on_click=open_link, )
            ],
            alignment=ft.MainAxisAlignment.END,
        )
