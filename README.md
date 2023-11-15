# ttrp-server_V2

## Description

This repo represent a new version for the server side of a tabletop roleplaying character creation service for dungeons and dragons 5th edition.
in this version I aim to rewrite the original application which was written in typescript into python instead.

## Some words on the status of the project

As I'm still learning and exploring what is possible with writing a server in python this application should not be seen as an ongoing experiment. 

because I’ve been asked to show this repo to certain curious spectators I've changed this repo’s availability to the public.
however it should be said that this is still very much an ongoing project and may incur changes from one day to another.

It’s also worth mentioning that because this project is a way to test and explore what can be done with python, that at any given time the application may not be a representation of what it is supposed to be according to the description.
As of 15/11-2023 this application is more of a REST API for a todo application rather than the dnd character sheet creator as described in the description.
If you want an idea of what it will look like in the end you can check out my [`ttrp-server`](#https://github.com/AxelElg/ttrp-server) written in typescript

## local setup

### requirements

To start this application you'll need to have python (=> v3.11.6) installed on your machine.
You'll also want to install flask using pip if you don't have it already.

if you want to set up a local virtual environment for this particular application and its required packages I recommend running the following commands in the terminal at the root of this project:

> python -m venv .venv
> source .venv/bin/activate

and then you can install flask using:

> pip install flask

After you've installed all  you can start up the application running the following command:

> python src/server.py

You should now have the server running at [`localhost:9005/`](#localhost:9005/)
