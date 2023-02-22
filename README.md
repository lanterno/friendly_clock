## Display time in a human-friendly format

### Running this project

The best way to understand what this code can do is to look at the `app/tests.py` file.

You can also run the tests using this command
```commandline
python -m app.tests
```

### Notes
The solution available in this repo should cover all the different cases for time.

One case I like in particular is the following

`23:55` -> `Five to Twelve AM`

The code is able to flip the time to use `5 to 12` but also able to know that
it switched from `PM` to `AM`.
