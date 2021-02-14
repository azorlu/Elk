import click
from runner import Runner

@click.command()
@click.option('--i', type=click.Path(exists=False), 
    default= "\\inventory.json", 
    help='path to requests inventory json file')
@click.option('--d', type=click.Path(exists=False), 
    default='\\driver\\chromedriver.exe', 
    help='path to Google Chrome driver file')
@click.argument('id', nargs=1)
def main(i, d, id):
    runner = Runner(i, d)
    result = runner.run_query(id)
    click.echo(result)

if __name__ == '__main__':
    main()