"""Console script for coinaddress."""
import sys
import click

from .networks import registry


@click.command()
@click.argument('network')
@click.argument('path', default='0', type=str)
@click.option('--xpub-file', default='-', type=click.File('r'))
@click.option('--xpub', default=None)
@click.option('--output', '-o', default='-', type=click.File('w'))
@click.option('--number', '--num', '-n', default=1, type=int,
              help="Number of addresses to generate")
def main(network, xpub, xpub_file, path, output, number=1):
    """Coin address generation CLI.

    You can generate one or multiple coin addresses from xpub.

    Supported NETWORK list:

    * `bitcoin` or `BTC`

    * `bitcoin_cash` or `BCH`

    * `ethereum` or `ETH`

    * `litecoin` or `LTC`

    * `ripple` or `XRP`

    `0` derivation path will be used by default. You can overwrite it using
    PATH argument. Last path index will be used as starting index if
    --number option passed.

    To generate 1000 addresses for bitcoin xpub from file (xpub should be
    a single line in this file):

        cat xpub.txt | coinaddress bitcoin 0 -n 1000

    To generate another bunch of addresses:

        cat xpub.txt | coinaddress bitcoin 1000 -n 1000

    xpub can be passed with `--xpub` option but you should avoid this and prefer
    read from file for security reasons.

    """
    if xpub is None:
        xpub = xpub_file.readline().strip()
    net = registry.get(network)
    path_parts = path.split('/')
    last_index = int(path_parts[-1])
    prefix = '/'.join(path_parts[:-1])
    for i in range(last_index, last_index + number):
        index_path = f'{i}'
        if prefix:
            index_path = f'{prefix}/{i}'
        result = net.get_address(xpub=xpub, path=index_path)
        output.write(result)
        output.write('\n')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
