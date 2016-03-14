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

### Requirements

The following setion outlines the requirements for running shownoter.

Shownoter uses the following technologies which will need to be installed on your system in addition to the modules in requirements.txt.

#### Python3
While we have tested *Shownoter* against python 2.7 previously, we ask that you use 3.5.1 to work with *Shownoter*.

#### Flask (with some extension)
*Shownoter* is a [***flask***](http://flask.pocoo.org) application.

#### MongoDB
    
    This version of shownoter is built using `MONGODB`.
    To install MongoDB please follow the instructions found at https://docs.mongodb.org/manual/installation/

    You will also need a interpretor for mongo in python. This module uses `[pymongo](http://api.mongodb.org/python/current/)`


## Getting Started

Here is a quick getting started guide. For more information be sure to check out the [*Shownoter* wiki](https://github.com/kjaymiller/shownoter/wiki). 

#### Create and Activate Virtualenv 
> `python -m venv <environment name>`

> `. bin/activate`

#### Install Requirements
Requirements to run Shownoter are stored in the file `requirements.txt`.  To install the required modules needed to run Shownoter perform the following command.

> ```pip install -r requirements.txt```

If you plan on developing Shownoter there are some additional requirements needed to do things like running tests.  These are stored in the file dev-requirements.txt.  You can install these with the following command:

> ```pip install -r dev-requirements.txt```

#### Modify config.py File
A `config.py` file has been included however you should provide your own secret key. 
**Shownoter will run with the default key in however this could leave your environment vulnerable**

#### Starting Shownoter
The first step in running shownoter is to start the application and the dbengine. 

- To start shownoter, simply run the `run.py` file.
  >  `python run.py`

- To start the mongoDB engine, you will need to run `mongod` located in `./bin/` in your Mongo directory.
    - you can also specify your dbpath by using the -flag `--dbpath <location>`
    > `<path-to-mongo-dir>/mongod --dbpath <desired db location>`
