# Demo project for the simple-pastebin-parser project

you can check out the project [here](https://github.com/shlomikushchi/simple-pastebin-parser)

installation:
---
local execution: 

`pip install -r requirements.txt`

will install the latest version of simple-pastebin-parser

run inside docker (make sure you have [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) installed)

run the project like this:
`docker-compose up`


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

v0.3.0 - Bonus 2
--- 
run the app inside a container

you can now use this command:
`docker-compose up`

the docker image will be built on top of python3.6.10-slim. that a container will be created, running the main.py file.
the result files will still be created in the `OUTPUT` folder. 


v0.4.0 - Bonus 3
--- 
store pastes to redis DB
- added another container with redis
- stored pastes to redis ( very simple POC )