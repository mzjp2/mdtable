# :clipboard: mdtable

![PyPI](https://img.shields.io/pypi/v/mdtable.svg?style=flat-square)
![License](https://img.shields.io/github/license/mzjp2/mdtable.svg?style=flat-square)
[![Code Style: Black](https://img.shields.io/badge/code-black-black.svg?style=flat-square)](https://github.com/ambv/black)

mdtable is a Python built command line interface that lets you convert csv files into Markdown formatted tables easily. It also provides a Python API to use for your projects.

## Installation

Run ``pip install mdtable`` and check that the latest version is current installed by running ``mdtable —version``.

## Usage

```shell
>>> mdtable [OPTIONS] INPUT_FILE
```

The options available are:

```
-a, --aligns TEXT  Comma seperated list of 'l,r,c'
-s, --save   TEXT  Path to save formatted markdown to
--delimiter  TEXT  Delimiter character in csv
--quotechar  TEXT  Quote character in csv
--escapechar TEXT  Escape character in csv
--writemode  TEXT  Python write mode, e.g w+, w, a, a+
--version          Show the version and exit.
--help             Show this message and exit.
```

**Example**:

Suppose you have a file `input.csv` like so:

```
Name,Department,Birthday Month
John Smith,Accounting,November
Erica Meyers,IT,March
Zain Patel,Engineering,June
Christopher Smith,Engineering,July
Kiseki Hirakawa,Human Resources,February
```

Running ``mdtable input.csv`` results in:

```
| Name              | Department      | Birthday Month |
| ----------------- | --------------- | -------------- |
| John Smith        | Accounting      | November       |
| Erica Meyers      | IT              | March          |
| Zain Patel        | Engineering     | June           |
| Christopher Smith | Engineering     | July           |
| Kiseki Hirakawa   | Human Resources | February       |
```

which looks like:

| Name              | Department      | Birthday Month |
| ----------------- | --------------- | -------------- |
| John Smith        | Accounting      | November       |
| Erica Meyers      | IT              | March          |
| Zain Patel        | Engineering     | June           |
| Christopher Smith | Engineering     | July           |
| Kiseki Hirakawa   | Human Resources | February       |

### API

[*soon*] more documentation

**Example**:

```python
from mdtable import MDTable

markdown = MDTable('in.csv')
markdown_string_table = markdown.get_table()
markdown.save_table('out.csv')
```

### Current Features

- [x] Ability to specify alignments, by providing a comma seperated string of alignments values (either 'l', 'r' or 'c') to ``mdtables —aligns [ALIGNS] INPUT_FILE``, say for example ``mdtables —aligns c,c,l input.csv``, there must be as many alignments characters as there are tables.
- [x] Ability to save output to a markdown file (and specify the writing mode) by providing the path to the file you wish to save to ``mdtables —save [SAVE_FILE] INPTUT_FILE`` say for example ``mdtables —save output.md input.csv``
- [x] Provide custom delimiter, quotation and escape characters for reading in your csv file. This is done by providing the character to ``—delimiter, —quotechar, —escapehcar`` respectively.

## Future Features

- [ ] Implement a raw centering flag to prettify the output if required
- [ ] Add a padding option to make table border padding customisable
- [ ] Add documentation for the API
