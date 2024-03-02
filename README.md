# Clippy

A clipboard that saves your previous clipboard items.

Press `CTRL+ALT+C` to open a GUI of your clipboard history. Click on any of the item to copy it to your clipboard.

### Installation

#### Use virtual environment

```
$ python -m venv env
$ source env/bin/activate
```

```
(env)$ pip install -r requirements.txt
```

### Running the program

```
(env)$ nohup python3 clippy.py > output.log 2>&1 &
```

Runs your Python script with `nohup` in the background and redirects both standard output and standard error to `output.log`.
