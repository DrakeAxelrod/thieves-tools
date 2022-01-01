import click


@click.group()
def example():
  pass

# if you use @example_grp.command() you dont need to register
@click.command()
@click.option("--name", "-n", default="World", help="the name of the person to greet")
def greet(name):
  # docs string for cli
  """
  this prints "Hello, {name}!"
  """
  click.echo("Hello, %s!" % name)

# register command
example.add_command(greet)
