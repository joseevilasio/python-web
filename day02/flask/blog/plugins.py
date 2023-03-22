from flask import Flask
from mistune import markdown


def configure(app: Flask):
    app.add_template_global(markdown)
    app.add_template_filter(lambda date: date.strftime("%d-%m-%Y"), "format_date")
