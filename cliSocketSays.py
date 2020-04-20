import click

from ipaddress import ip_address

from socket_says.socket_says import SocketSays


#@click.group()
@click.command()
@click.option('-a', '--addr', default=None,
              help='Address to connect to')
@click.option('-p', '--port', default=None,
              help='Port to connect on')
@click.option('-t', '--text', default="",
              help='Text to send (can be multiline)')
def cliSocketSays(addr, port, text):
    if addr and port and text != "":
        print("Going for it")
        simon = SocketSays(addr, port)
        simon.says(text)
        simon.listens()
    else:
        "\nPlease make sure you include the required parameters. Use '--help' "



if __name__ == "__main__":
    cliSocketSays()
