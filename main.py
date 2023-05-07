import flet as ft
import pandas as pd
from utils import *
from custom_widgets.list_upper_sections import TitleText, SubtitleText, SubscriptionButton
from custom_widgets.card import ArticleCard


async def get_data():
    df = pd.read_csv("BlogData.csv")
    return df


async def main(page: ft.Page):
    page.padding = 2
    page.fonts = fonts
    page.title = title
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    lv = ft.ListView(expand=True, spacing=10, padding=15)

    article_data = await get_data()

    for i in range(0, article_data.shape[0]):
        lv.controls.append(
            ArticleCard(
                title=article_data.Title[i],
                title_font_family=title_font,
                desc=article_data.Description[i],
                desc_font_family=desc_font,
                link=article_data.Link[i],
            )
        )

    await page.add_async(
        ft.Container(
            ft.Column([
                TitleText(text=title, font_family=title_font),
                SubtitleText(text=subtitle, font_family=desc_font),
                SubscriptionButton(
                    button_text=subscription_button_text,
                    link=subscription_form_link
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ), padding=10,
        ),
        lv
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080, assets_dir="assets")
