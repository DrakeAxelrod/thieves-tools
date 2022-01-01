from re import M
from bs4.element import Tag
import click
import requests
import webview
from bs4 import BeautifulSoup
import json

def remove_html_tags(soup: BeautifulSoup, list: list):
    for tag in list:
        t: Tag
        for t in soup.find_all(tag):
            t.decompose()

def open_window(html: str):
    window = webview.create_window(
        "Cheatsheet", html=html, frameless=True, fullscreen=True)

    def close():
        window.destroy()
    window.expose(close)

    def addListener(window):
        window.evaluate_js(
            "document.addEventListener('keydown', (e) => { if (e.key === 'Escape') pywebview.api.close() });")
    webview.start(addListener, window, debug=True)


def generate_window(query):
    soup = BeautifulSoup(query.text, "lxml")
    remove_html_tags(soup, ["iframe", "footer", "header"])
    soup.find("nav").decompose()
    soup.find("summary").decompose()
    soup.find("div", {"class", "container"}).decompose()
    open_window(str(soup))

@click.command()
@click.option("--name", "-n", help="Display a cheatsheet from devhints.io based on passed name")
def cheatsheet(name: str):
    result = requests.get("https://www.devhints.io")
    soup = BeautifulSoup(result.text, "lxml")
    tag: Tag
    options = {}
    for tag in soup.find_all("a", {"class", "article"}):
        item = json.loads(tag.attrs['data-js-searchable-item'])
        if item['category'] not in options:
            options[item['category']] = [item['slug']]
        else:
            options[item['category']].append(item['slug'])
    if name.capitalize() in options.keys():
        result = requests.get("https://www.devhints.io/%s" % name)
        generate_window(result)
    else:
        categories: list = []
        click.echo(click.style("categories", fg="blue"))
        for i, option in enumerate(options.keys()):
            categories.append(option)
            click.echo(f"{i + 1}. {option.lower()}")
        ans = click.prompt("category")
        category = categories[int(ans) - 1]
        click.echo(click.style("Options", fg="blue"))
        opts: list = []
        for i, option in enumerate(options[category]):
            opts.append(option)
            opt = option.replace(category.lower() + "/", "")
            click.echo(f"{i +1 }. {opt}")
        ans = click.prompt("option")
        query = opts[int(ans) - 1]
        result = requests.get("https://www.devhints.io/%s" % query)
        generate_window(result)
