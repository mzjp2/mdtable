#  pylint: disable=missing-docstring,invalid-name,unused-variable

import os
import pytest
from mdtable.mdtable import MDTable, handle_aligns

INPUT = "tests/data/in.csv"


def test_simple_output():
    table = MDTable(INPUT)
    with open("tests/data/out.md", "r") as f:
        OUTPUT = f.read()
    assert OUTPUT == table.get_table()


def test_align_output():
    table = MDTable(INPUT, aligns=("c", "r", "l"))
    with open("tests/data/out_align.md", "r") as f:
        OUTPUT = f.read()
    assert OUTPUT == table.get_table()


def test_padding_output():
    table = MDTable(INPUT, padding=3)
    with open("tests/data/out_padded.md", "r") as f:
        OUTPUT = f.read()
    assert OUTPUT == table.get_table()


def test_padding_align_output():
    table = MDTable(INPUT, padding=3, aligns=("c", "r", "l"))
    with open("tests/data/out_padded_align.md", "r") as f:
        OUTPUT = f.read()
    print(OUTPUT)
    print(table.get_table())
    assert OUTPUT != table.get_table()


def test_align_validate_length():
    with pytest.raises(
        ValueError,
        match="You need to specify the alignment for all columns. There are 3 columns, but you provided 2 alignments",
    ):
        table = MDTable(INPUT, aligns=("c", "r"))


def test_align_validate_input():
    with pytest.raises(
        ValueError,
        match="Aligns must be a tuple of 'l', 'r' and 'c' for left, right and centre. Found x instead",
    ):
        table = MDTable(INPUT, aligns=("x", "e", "f"))


def test_align_validate_input_complicated():
    with pytest.raises(
        ValueError,
        match="Aligns must be a tuple of 'l', 'r' and 'c' for left, right and centre. Found gdfgsd instead",
    ):
        table = MDTable(INPUT, aligns=("l", "gdfgsd", "f"))


def test_handle_aligns_default():
    assert handle_aligns("") is None


def test_handle_aligns():
    assert handle_aligns("l,r,c") == ("l", "r", "c")


def test_handle_aligns_complicated():
    assert handle_aligns("l,   r, C, R") == ("l", "r", "c", "r")


def test_save_file():
    table = MDTable(INPUT)
    table.save_table("tests/data/temp.md")
    assert os.path.exists("tests/data/temp.md")


def test_save_file_contents():
    with open("tests/data/temp.md", "r") as f:
        with open("tests/data/out.md", "r") as g:
            assert f.read() == g.read()
    os.remove("tests/data/temp.md")


def test_get_max_word_col():
    table = MDTable(INPUT)
    correct = {0: 17, 1: 15, 2: 14}
    assert table._word_length_dict == correct  # pylint: disable=protected-access


def test_imports():
    from mdtable import MDTable as x  # pylint: disable=unused-import
