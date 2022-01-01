import click
import subprocess

@click.command()
@click.argument("query", nargs=-1)
def question(query):
  question = "/".join(query)
  subprocess.call(f"cht.sh gaca{question}", shell=True,)
