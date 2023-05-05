import flet as ft
from card import ArticleCard
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


async def get_data():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open("My Articles").sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data, columns=data[0])
    return df


async def main(page: ft.Page):
    page.title = "ListView"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    lv = ft.ListView(expand=1, spacing=10, padding=20)

    article_data = await get_data()

    for i in range(0, article_data.shape[0]):
        lv.controls.append(
            ArticleCard(page, article_data.Title[i], article_data.Author[i], article_data.Link[i])
        )

    await page.add_async(
        ft.Container(
            ft.Column([
                ft.Text(value="Subhradeep's Articles",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        ),
                ft.Text(
                    value="Here I listed all of my Data Science Articles I wrote till now. Don't forget to check it out!",
                    size=15,
                    ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ), padding=20,
        ),
        lv
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)
