import flet as ft


class TitleText(ft.UserControl):
    def __init__(self, text: str, font_family: str = None):
        super().__init__()
        self.text = text
        self.font_family = font_family

    def build(self):
        return ft.Text(
            value=self.text,
            size=32,
            weight=ft.FontWeight.BOLD,
            font_family=self.font_family,
            text_align=ft.TextAlign.CENTER
        )


class SubtitleText(ft.UserControl):
    def __init__(self, text: str, font_family: str = None):
        super().__init__()
        self.text = text
        self.font_family = font_family

    def build(self):
        return ft.Text(
            value=self.text,
            size=16,
            font_family=self.font_family,
            text_align=ft.TextAlign.CENTER
        )


class SubscriptionButton(ft.UserControl):
    def __init__(self, button_text: str, link: str, font_family: str = None):
        super().__init__()
        self.button_text = button_text
        self.link = link
        self.font_family = font_family

    def build(self):
        async def on_button_click(e):
            await self.page.launch_url_async(self.link)

        return ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.SUBSCRIPTIONS),
                ft.Text(self.button_text, font_family=self.font_family)
            ], wrap=True),
            on_click=on_button_click
        )
