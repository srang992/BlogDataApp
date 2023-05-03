import webbrowser
import flet as ft


def open_link(e):
    webbrowser.open_new_tab("https://www.analyticsvidhya.com/blog/2022/05/scraping-jobs-on-linkedin-using-scrapy/")


def main(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    button = ft.ElevatedButton("Open Link",
                               on_click=open_link)
    page.add(
        button
    )


ft.app(target=main)

