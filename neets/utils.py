import os
from rich.console import Console

def check_api_key():
    console = Console()
    api_key = os.getenv('NEETS_API_KEY')

    if api_key == None:
        console.print("\n[red]Error:[/red] No API key found. Set your API key using:")
        console.print("\n\t[bold]export NEETS_API_KEY=[/bold][yellow]your-api-key[/yellow]")
        console.print("\nYou can find your API key at [link=https://neets.ai]https://neets.ai[/link]\n")
        return False

    return True