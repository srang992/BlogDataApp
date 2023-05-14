import flet as ft
from utils import *
import feedparser
from custom_widgets.list_upper_sections import TitleText, SubtitleText, SubscriptionButton
from custom_widgets.card import ArticleCard
from bs4 import BeautifulSoup


async def get_data():
    medium_feed = feedparser.parse("https://medium.com/feed/@srang992")
    av_data = feedparser.parse("https://www.analyticsvidhya.com/blog/author/subhradeep06/feed/")
    return medium_feed, av_data


async def main(page: ft.Page):
    page.padding = 2
    page.fonts = fonts
    page.title = title
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    lv = ft.ListView(expand=True, spacing=10, padding=15, )

    lv.controls.append(
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
    )

    medium_data, av_data = await get_data()

    for entry1 in medium_data.entries:
        soup = BeautifulSoup(entry1.description, "html.parser")
        lv.controls.append(
            ArticleCard(
                title=entry1.title,
                title_font_family=title_font,
                desc=soup.text,
                desc_font_family=desc_font,
                link=entry1.link,
            )
        )

    for entry2 in av_data.entries:
        soup = BeautifulSoup(entry2.description, "html.parser")
        lv.controls.append(
            ArticleCard(
                title=entry2.title,
                title_font_family=title_font,
                desc=soup.text,
                desc_font_family=desc_font,
                link=entry2.link,
            )
        )

    await page.add_async(
        lv
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080, assets_dir="assets")
