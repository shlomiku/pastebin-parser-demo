[![Build Status](https://travis-ci.org/shlomikushchi/Simple-Pastebin-Parser.svg?branch=master)](https://travis-ci.org/shlomikushchi/Simple-Pastebin-Parser)

# Demo project for the simple-pastebin-parser project

you can check out the project [here](https://github.com/shlomikushchi/simple-pastebin-parser)

installation:
---
`pip install -r requirements.txt`

will install the latest version of simple-pastebin-parser

  Release notes:
===

v0.1.0 - basic requirements
---
basic required implementation.

using the simple-pastebin-parser to sample pastebin.com every 2 minutes and storing the files to an OUTPUT local folder. 

run it like so: `python main.py`



v0.2.0 - Bonus 1
---
upgraded simple-pastebin-parser to v0.5.0

Each one of the paste model's parameters must be normalized.
For example:
* Author - In cases it's Guest, Unknown, Anonymous, etc... the author name must be the same, for example: "" (empty string)
* Title - Same as with Author.
* Date - UTC Date
* Content - Must be stripped of trailing spaces.

run it like so: `python main.py