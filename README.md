# Shownoter
Organize and format your references into markdown with ease.

## *Shownoter wants to help you*

Shownoter is designed to take plain text and give you a formatted list of links and images. This will format your references that will help you prepare those shownotes.

## How does it work?

Sometimes important information is buried in random text.  A good example of this is a chat history for your hangout or podcast.

Take for instance the following example:

```
Jay: I have been really interested in playing battleship online.
Jamal: Yeah battleship is the best, I found this great game at LessThanTwoPlayerBattleship.com
Jay: That is great, I will check it out
Jay: BTW, I found this great site for helping boost productivity GoTeamTypingCatGo.net
Jamal: Thanks man, I am really excited about checking that out.

```

Afterward you want to add these links to your shownotes, but there has to be an easier way than sifting through all of the chat.

Once you find the links you will want to format them and give the links an appropriate name.

This is a lot of tedious work, but Shownoter will do it for you.

Shownoter will take the chat above and output a formatted list with descriptions like the following.

* [The home of 1.7 player battleship](LessThanTwoPlayerBattleship.com)
* [Go! Team typing cat Go! Homepage](GoTeamTypingCatGo.net)

## License
Shownoter is Licensed Under the Apache License, Version 2.0.
Please visit http://www.apache.org/licenses/LICENSE-2.0.html for more information.

## Requirements

The following setion outlines the requirements for running shownoter.

Shownoter uses the following technologies which will need to be installed on your system in addition to the modules in requirements.txt.

* Python 3 

### MongoDB
This version of shownoter is built using `MONGODB`.
To install MongoDB please follow the instructions found at https://docs.mongodb.org/manual/installation/

You will also need a interpretor for mongo in python. This module uses `[pymongo](http://api.mongodb.org/python/current/)`

### Python modules

Requirements to run Shownoter are stored in the file requirements.txt.  To install the required modules needed to run Shownoter perform the following command.

```pip install -r requirements.txt```

### Development requirements

If you plan on developing Shownoter there are some additional requirements needed to do things like running tests.  These are stored in the file dev-requirements.txt.  You can install these with the following command:

```pip install -r dev-requirements.txt```

## Testing

Shownoter uses automated tests to monitor and ensure the health of the project. Below are the ways to run the different sorts of tests for Shownoter.

### Test setup

Before running the tests you will need to install the dev-requirements as outlined above.  Additionally, you will need to install the module in editable mode: ```pip install -e .```

### Running unit tests

To run unit tests, use the following command:

```python -m pytest test```

### Running functional tests

To run functional tests, use the following command:

```python -m pytest functional```

### Running both unit and functional tests

The previous two commands can be combined, this is recommended when preparing for a pull request, but as functional tests take longer is not recommended during the normal TDD cycle.

```python -m pytest test functional```

### Running the linter

Linters do static analysis to find potential issues or style problems in the code.  To run the linter use the following command:

```python -m pylint app```

### Testing coverage

Test coverage can be determined using the pytest-cov plugin.  Use it as follows:

```
python -m pytest --cov-report term-missing --cov=app test/test_shownoter.py
```
