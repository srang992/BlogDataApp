import flet as ft
from card import ArticleCard
import pandas as pd


async def get_data():
    df = pd.read_csv("BlogData.csv")
    return df


async def main(page: ft.Page):
    page.fonts = {
        "Courgette": "fonts/Courgette-Regular.ttf",
        "Alkatra": "fonts/Alkatra-Regular.ttf"
    }
    page.title = "My Articles"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    lv = ft.ListView(expand=1, spacing=10, padding=20)

    article_data = await get_data()

    for i in range(0, article_data.shape[0]):
        lv.controls.append(
            ArticleCard(page, article_data.Title[i], article_data.Description[i], article_data.Link[i])
        )

    await page.add_async(
        ft.Container(
            ft.Column([
                ft.Text(value="Subhradeep's Articles",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        font_family="Courgette"
                        ),
                ft.Text(
                    value="Here I listed all of my Data Science Articles I wrote till now. Don't forget to check it out!",
                    size=16,
                    font_family="Alkatra",
                    ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ), padding=20,
        ),
        lv
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080, assets_dir="assets")
