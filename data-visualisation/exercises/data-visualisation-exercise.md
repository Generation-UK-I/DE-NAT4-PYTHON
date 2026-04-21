# Jupyter Notebook Exercise

## Part 1 - Setting up

### Part 1.0 - Venv and libs

Setup a venv:

1. Open the `handouts` folder in VSCode
1. Create a virtual environment with python by running:
    - `python3 -m venv .venv` (MacOS / Unix)
    - `py -m venv .venv` (Windows)
    - `python3 -m venv .venv` (GitBash)
1. Activate the virtual environment by running:
    - `source .venv/bin/activate` (MacOS / Unix)
    - `.venv\Scripts\activate` (Windows)
    - `source .venv/Scripts/activate` (GitBash)
1. Install our dependencies with
    1. `python3 -m pip install matplotlib ipykernel` (MacOS / Unix)
    1. `py -m pip install msvc-runtime matplotlib ipykernel` (Windows)
    1. `python -m pip install msvc-runtime matplotlib ipykernel` (GitBash)

Make a new notebook:

1. Install the Jupyter extension for VSCode (if you haven't already)
1. Create a new Jupyter Notebook file (`.ipynb`) in the `handouts` folder e.g. `exercises.ipynb`
1. Open your Jupyter Notebook in VSCode
1. Don't do anything else - yet!

### Part 1.1 - Checking the Notebook is working

Find the Python executable for your venv:

- Open a terminal in your `handouts` folder
    - Run `which python3` (MacOS / Unix)
    - Run `get-command python` (Windows Powershell)
    - Run `which python` (GitBash)
- You should get a result with a path like this:
    - `handouts\.venv/bin/python` (MacOS / Unix)
    - `handouts\.venv\Scripts\python` (Windows)
    - `handouts\.venv\Scripts\python` (GitBash)

Add your venv to the master list in VS Code:

1. Open the Command Palette
1. Search for `> Python: Select Interpreter`
1. Choose `Create Virtual Environment`
1. Choose `Venv`
1. Choose `Enter Interpreter Path`
1. Select your python executable in your `.venv` folder:
    - This should match the result of your "Find" step, above
    - `handouts\.venv/bin/python` (MacOS / Unix)
    - `handouts\.venv\Scripts\python` (Windows)
    - `handouts\.venv\Scripts\python` (GitBash)

Try and use your notebook:

1. Open your notebook
1. Click on the `Select kernel` button top-right
    1. Choose `Select Another Kernel`
    1. Choose `Python Environments`
    1. _Select the one that you added in **"Part 1.0"** above_
1. Add a Python codeblock in the Notebook
    1. In it add a basic code snippet like `print("Hello world")`
    1. Execute it using the "Play" or ">" arrow button
1. You may get VSCode saying it needs to install additional libraries:
    1. If so, click "Yes" or "Install", as appropriate

## Part 2 - Loading the Data

The following code loads the `titanic-data.csv` file into a dictionary called `titanic_data`. It will store 'age', 'sex', 'pclass', and 'survived' data for further analysis.

1. Paste this code into a new codeblock and execute it

    ```py
    import csv

    with open('titanic-data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        titanic_data = {'age': [], 'sex': [], 'pclass': [], 'survived': []}
        for row in reader:
            if row['age'] != '?':
                titanic_data['age'].append(float(row['age']))
            titanic_data['sex'].append(row['sex'])
            titanic_data['pclass'].append(int(row['pclass']))
            titanic_data['survived'].append(row['survived'])
    ```

## Part 3 - Plotting Age Distribution

Create a histogram to visualise the distribution of passenger ages.

1. _Hint:_ Use the import `import matplotlib.pyplot as plt`
1. _Hint:_ Use `plt.hist()` function for creating a histogram. Use `titanic_data['age']` as the data input, and set the number of bins (`bins = 10`) to get a clearer view of the distribution
1. Change the number of `bins` and run it again
    1. What changes?
    1. What does that mean for your data visualisation?

If you have problems with this running, check your import is correct, and check that the "kernel" you are using matches where pip installed your dependencies (see Part 1.0 and 1.1).

## Part 4 - Plotting Gender Distribution

1. Create a bar chart to visualise the number of male and female passengers
    1. _Hint:_ Use the `Counter` class from the `collections` module to count the number of male and female passengers
    1. _Hint:_ Then, use `plt.bar()` to create the chart with appropriate labels for the x-axis

## Part 5 - Plotting Class Distribution

Create a pie chart to visualise the distribution of passenger classes (1st, 2nd, and 3rd class).

1. _Hint:_  Use the `Counter` class to count the number of passengers in each class
1. _Hint:_ Then, use `plt.pie()` to create the chart, and add a legend to show which slice represents each class

## Part 6 - Analysing Survival Rates by Class (Extension)

Create a bar chart to visualise the survival rates for passengers in each class (1st, 2nd, and 3rd class)

1. _Hint:_ First, calculate the number of survivors and total passengers in each class using list comprehensions and the `Counter` class from the `collections` module
1. _Hint:_ Calculate the survival rates by dividing the number of survivors by the total passengers in each class
1. _Hint:_ Use `plt.bar()` to create the bar chart with appropriate labels for the x-axis, and set the y-axis range between 0 and 1 to represent the survival rates as percentages
1. _Additional hint:_ Set a title for the plot using `plt.title()`, and label the y-axis using `plt.ylabel()`. Customize the plot further by setting the x-axis labels to "1st Class", "2nd Class", and "3rd Class"
