import click

from lib import cheatsheet, question

# @click.group(invoke_without_command=True)
@click.group()
@click.pass_context
@click.help_option("-h", "--help")
def cli(ctx):
  """
  Should fill this in :P
  """
  pass


cli.add_command(cheatsheet)
cli.add_command(question)

