# espirometro


# How to set up the environment and run the App

## Create a Python Virtual Environment and Install the Dependencies

Install `virtualenv`, create and active the `venv` environment:

```
$ pip install virtualenv
$ virtualenv venv

$ source venv/bin/activate # Activate on Mac OS / Linux
$ venv\Scripts\activate    # Activate on Windows
```

After the virtual environment is activated, install the dependencies:

```
$ pip install -r requirements.txt
$ pip install .
```

## Running the game

```
$ python -m flappy.main
```
