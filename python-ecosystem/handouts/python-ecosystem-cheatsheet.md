# Python Ecosystem cheatsheet

## Modules

`import` imports a module
`from` import a specific thing from module

```python
# imports everything from module1
import module1
# import only print_name function
from module1 import print_name
```

## Package Manager (pip)

`pip install` downloads/installs a dependency
`pip list` list all dependencies
`pip uninstall` removes/uninstalls a dependency

Unix/MacOS:

```sh
$ pip --version
$ pip install requests
$ pip list
$ pip uninstall requests
```

Windows:

```sh
$ py -m pip --version
$ py -m pip install requests
$ py -m pip install requests
$ py -m pip list
$ py -m pip uninstall requests
```

## Virtual Environments

`venv` is a python module that creates a virtual environment

### Create venv

```sh
# Mac/Unix
$ python3 -m venv .venv
# or on Windows
$ py -m venv .venv
```

### Activate/Deactivate venv

Windows:

```sh
# activate the virtual environment
$ .venv\Scripts\activate.bat
# deactivate the virtual environment
$ deactivate
```

Unix/MacOS:

```sh
# activate the virtual environment
$ source .venv/bin/activate
# deactivate the virtual environment
$ deactivate
```

### Manage Packages

`pip freeze` snapshot of current package dependencies
`pip install -r` downloads/installs a dependency from a given file
`pip install --upgrade` updates a dependency

```sh (Windows or Unix)
# store the current package dependencies from the virtual environment in requirements.txt
(.venv) $ pip freeze > requirements.txt
# install the package dependencies found in requirements.txt to the virtual environment
(.venv) $ pip install -r requirements.txt
# install request version 2.6.0 to the virtual environment
(.venv) $ pip install requests=2.6.0
# list all packages in the virtual environment
(.venv) $ pip list
# update the requests dependency in the virtual environment
(.venv) $ pip install --upgrade requests
# uninstall the request dependency from the virtual environment
(.venv) $ pip uninstall requests
```
