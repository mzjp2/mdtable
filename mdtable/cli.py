"""This implements the command line interface for mdtable"""
import click

from mdtable.mdtable import MDTable, handle_aligns, __version__


@click.command()
@click.argument("input_file")
@click.option("--aligns", "-a", help="Comma seperated list of 'l,r,c'", default="")
@click.option(
    "--padding", "-p", help="Padding for raw Markdown Table formatting", default=1
)
@click.option("--save", "-s", help="Path to save formatted markdown to", default="")
@click.option("--delimiter", help="Delimiter character in csv", default=",")
@click.option("--quotechar", help="Quote character in csv", default='"')
@click.option("--escapechar", help="Escape character in csv", default="")
@click.option("--writemode", help="Python write mode, e.g w+, w, a, a+", default="w")
@click.version_option(version=__version__)
def main(
    input_file, aligns, padding, save, delimiter, quotechar, escapechar, writemode
):  # pylint: disable=missing-docstring, too-many-arguments
    aligns = handle_aligns(aligns)
    if padding == 0:
        raise ValueError("0 padding is currently not enabled. Try again later.")

    table = MDTable(
        input_file,
        aligns,
        padding=padding,
        delimiter=delimiter,
        quotechar=quotechar,
        escapechar=escapechar,
    )
    if not save:
        print(table.get_table())
    else:
        table.save_table(save, writemode)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
