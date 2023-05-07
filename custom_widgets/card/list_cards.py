import flet as ft
from .card_sections import CardDetails, CardButtons


class ArticleCard(ft.UserControl):
    def __init__(self, title: str,
                 title_font_family: str,
                 desc: str, desc_font_family: str,
                 link: str):
        super().__init__()
        self.title = title
        self.title_font_family = title_font_family
        self.desc = desc
        self.desc_font_family = desc_font_family
        self.link = link

    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        CardDetails(
                            title=self.title, desc=self.desc,
                            title_font_family=self.title_font_family,
                            subtitle_font_family=self.desc_font_family,
                        ),
                        CardButtons(link=self.link, font_family=self.title_font_family)
                    ],
                ),
                padding=10,
            )
        )
