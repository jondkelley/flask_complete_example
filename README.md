# Flask Complete Example

The purpose of this webapp is to show a structured example of a flask app with user registration and simple templates

## Installation

First, you need to clone this repo:

```bash
$ git clone git@github.com:jondkelley/flask-complete-example.git
```

Or:

```bash
$ git clone https://github.com/jondkelley/flask-complete-examplegit
```

Then change into the `flask-complete-example` folder:

```bash
$ cd flask-complete-example
```

Now, we will need to create a virtual environment and install all the dependencies. We have two options available for now.

Use Pipenv:

```bash
$ pipenv install
$ pipenv shell
```

Or use pip + virtualenv:

```bash
$ virtualenv venv
$ . venv/bin/activate  # on Windows, use "venv\Scripts\activate" instead
$ pip install -r requirements.txt
```

## How to Run a Specific Example Application?

**Before run a specific example application, make sure you have activated the virtual enviroment:**

```bash
$ cd flask-examples
$ pipenv shell  # or ". venv/bin/activate" / "venv\Scripts\activate" (Windows)
```

For example, if you want to run the Hello application, just execute these commands:

```bash
$ cd hello
$ flask run
```

Similarly, you can run HTTP application like this:

```bash
$ cd http
$ flask run
```

This app starts at http://localhost:5000.

## Advanced Examples Flask Applications

- [SayHello](https://github.com/greyli/sayhello): A simple message board.
- [Bluelog](https://github.com/greyli/bluelog): A blog engine that supports category and resource management.
- [Albumy](https://github.com/greyli/albumy): A full-featured photo-sharing social networking.
- [Todoism](https://github.com/greyli/todoism): A to-do application implements as SPA, it supports i18n and provides web APIs.
- [CatChat](https://github.com/greyli/catchat): A chat room based on WebSocket.

## Contributions

Any contribution is welcome, just fork and submit your PR.
