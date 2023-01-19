# PytestFramework
 PytestFramework using pom

## Setup
This project requires an up-to-date version of Python 3.
It also uses [conda](https://docs.conda.io) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository and open the project in the terminal.
2. Run `conda env create --file Config/environment.yml` from the command line in the project's root directory (it will create virtual env with all dependencies available in the environment.yml file).
3. After virtual env created, select it on your IDE or To activate this project's virtualenv , run `conda activate PytestFrameworkEnv`.
4. If you update or install any new package so update Config/environment.yml file also by using command `conda env export --file Config/environment.yml`

## Setup env variables locally
At the root of the project (Inside PytestFramework), create the file .env Note: don't commit this file.
Add the following variables in .env file
```
BASE_URL=
AWS_IOT_URL=
AWS_IOT_USERNAME=
AWS_IOT_PASSWORD=
AWS_Console_URL=
AWS_Console_ACCOUNT_ID=
AWS_Console_USERNAME=
AWS_Console_PASSWORD=
```


## Running Tests by command line or terminal
Run tests simply using the `pytest` command.
Depending upon your environment, it may be better to use `python -m pytest`.
To Run parallel test run pytest xdist command, run `python -m pytest -n 2`
Run the following command to generate pytest html reports `python -m pytest -v -rs --html=Reports/PytestHtmlReport/report.html --self-contained-html`

## More Info

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.
If you want to manually run all pre-commit hooks on a repository, run `pre-commit run --all-files`, To run individual hooks use `pre-commit run <hook_id>`.




