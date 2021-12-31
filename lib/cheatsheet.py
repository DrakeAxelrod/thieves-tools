import click

@click.command()
@click.option("query")
def devhints(query):
  click.echo(f"hello from cheatsheet ${query}")

if __name__ == "__main__":
  devhints()
