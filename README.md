# football-team-analysis

## About

The aim of this repo is to scrape footfall data/statistics from various sources, process, evaluate and visualize them with regard to various KPIs. In this repo, the KPIS are focused on the football style of 1.FC Köln and will be analyzed further below. 


## Data Flow

Two websites serve as data sources. The first is FBref.com, which provides a very wide range of statistics and other data on Bundesliga teams and players for the last seasons. These values are based on the provider Statsbomb. 
On the other hand, the sport.de website is used to obtain information on the running values of the individual teams.
After the data has been scraped, the raw data is saved in a csv format to be cleansed in the next step. Here, unnecessary information that is not required is removed.
The cleansed data from the current season and the previous season is then used to perform the analysis. 
The data flow diagram is shown below. 

![About](images/dataflow.jpg)


## Analysis

As a preface, I would like to point out that the analysis naturally has its limits. The analysis is only possible to the extent that the freely available data allows, and even this data should be treated with caution because the exact definitions behind it are not always known. 
Of course, there is much more data and data types, but these are difficult or even impossible to obtain for private projects. 
That's why I focused on the information that I was able to obtain. 

In order to be able to analyze FC Köln, I first had to understand a few of the FC's playing ideas and I tried to shed light on a few things from this perspective. Especially in comparison to the current season, where FC Köln has not yet been able to build on its performance as in the previous season when it finished in 11th place.

The interesting thing for FC Köln, whose style of play is based on pressing, is to look at key figures such as ball recoveries, running data and tackles. On the offensive side, crosses are a popular means of setting up the powerful strikers. 

The statistics and analysis are a start, but it has its limitations. With better data, for example, KPIs could be developed to classify pressing behavior in a score to see how well 1.FC Köln presses. However, data such as ball conquests per minute, opponent's ball possession, defensive actions in general per minute in ball possession would be necessary for development.





## Getting Started

To set up your local development environment, please run:

    poetry install

Behind the scenes, this creates a virtual environment and installs `football_team_analysis` along with its dependencies into a new virtualenv.
Whenever you run `poetry run <command>`, that `<command>` is actually run inside the virtualenv managed by poetry.

You can now import functions and classes from the module with `import football_team_analysis`.

### Testing

We use `pytest` as test framework. To execute the tests, please run

    pytest tests

To run the tests with coverage information, please use

    pytest tests --cov=src --cov-report=html --cov-report=term

and have a look at the `htmlcov` folder, after the tests are done.

### Notebooks

You can use your module code (`src/`) in Jupyter notebooks (`notebooks/`) without running into import errors by running:

    poetry run jupyter notebook

or

    poetry run jupyter-lab

This starts the jupyter server inside the project's virtualenv.

Assuming you already have Jupyter installed, you can make your virtual environment available as a separate kernel by running:

    poetry add ipykernel

    poetry run python -m ipykernel install --user --name="football-team-analysis"

Note that we mainly use notebooks for experiments, visualizations and reports. Every piece of functionality that is meant to be reused should go into module code and be imported into notebooks.

### Distribution Package

To build a distribution package (wheel), please use

    python setup.py bdist_wheel

this will clean up the build folder and then run the `bdist_wheel` command.

### Contributions

Before contributing, please set up the pre-commit hooks to reduce errors and ensure consistency

    pip install -U pre-commit

    pre-commit install

If you run into any issues, you can remove the hooks again with `pre-commit uninstall`.

## Contact

Mark Vollmer (mark-vollmer@web.de)

## License

© Mark Vollmer
