# Advent-of-Code-2024
Solutions for AoC 2024

## setup.py
setup.py downloads your input file for the day from the Advent of Code website and genarates a template file for your code.<br>
To use, create a file called .env as so:
```
AOC_SESSION=""
```
Set AOC_SESSION to your Advent of Code session cookie. This is necessary to retrieve the input file.<br>
In setup.py, you can change the filename and template content for your template file.<br>
Then, run the following commands:
```
pip install python-dotenv
pip install pytz
```
To use, run:
```
python setup.py
```