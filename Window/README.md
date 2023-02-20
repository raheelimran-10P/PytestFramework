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

## Add telenium and python-jsonrpc in your env
Run the below command after activating virtual env.
Run `pip install telenium`.
Run `pip install python-jsonrpc`.

## Run your application with telenium client
Go to your application repo, cd to main.py path
Run `python -m telenium.execute main.py`.
Now, run your pytest test cases.
