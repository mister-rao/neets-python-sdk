import click
from rich.console import Console
from neets.completions import send_request

NEETS_API_CLI_VERSION = "0.0.1"

@click.group()
@click.version_option(NEETS_API_CLI_VERSION, message='Neets api cli version: %(version)s')
def cli():
    pass


@cli.command()
@click.option('--prompt', '-p', help='The prompt to use for the model.', required=True)
@click.option('--instructions', '-i', help='The instructions to use for the model.', default="")
@click.option('--model', '-m', help='The model to use for the completion.', default="Neets-7B")
@click.option('--max-tokens', '-mt', help='The maximum number of tokens to generate.', default=500)  
def chat(prompt, instructions, model, max_tokens):
    send_request(prompt, instructions, model, max_tokens)
