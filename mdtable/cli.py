"""This implements the command line interface for mdtable"""
import click

from mdtable.mdtable import MDTable, handle_aligns


@click.command()
@click.argument("input_file")
@click.option("--aligns", "-a", help="Comma seperated list of 'l,r,c'", default="")
@click.option("--save", "-s", help="Path to save formatted markdown to", default="")
@click.option("--delimiter", help="Delimiter character in csv", default=",")
@click.option("--quotechar", help="Quote character in csv", default='"')
@click.option("--escapechar", help="Escape character in csv", default="")
@click.option("--writemode", help="Python write mode, e.g w+, w, a, a+", default="w")
def main(
    input_file, aligns, save, delimiter, quotechar, escapechar, writemode
):  # pylint: disable=missing-docstring, too-many-arguments
    aligns = handle_aligns(aligns)
    table = MDTable(
        input_file,
        aligns,
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