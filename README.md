# Selenium Python - take screenshot

A Selenium python project that opens www.google.com in a Chrome web browser and takes a screenshot.

## Prerequisites

* Install Google [Chrome](https://www.google.com/chrome/)
* Install Selenium Chrome WebDriver- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
* Install [Python3.7](https://www.python.org/downloads/)
* Install the python required modules from `requirements.txt` - `pip install -r requirements.txt`
  * In case you are using [pipenv](https://docs.pipenv.org/en/latest/) a Pipfile is also included
    * create a virtual environment - `pipenv --python 3.7`
    * install requirements - `pipenv install`

## Running the project

Run the `ggl.screenshot.py` with the python 3.7 interpreter according to your setup. For example:

* using system's default python3 - `python3 ggl.screenshot.py`
* using pipenv - `pipenv run python3 ggl.screenshot.py`

Screenshot will be saved as `ggl.screenshot.png` in your working directory.
