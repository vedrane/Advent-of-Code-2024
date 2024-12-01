import os
import datetime
import urllib.request

from dotenv import load_dotenv
import pytz

# Load the environment variables from .env
load_dotenv()

# Get the day
d = datetime.datetime.now(pytz.timezone('US/Eastern')).day
# Input file url
url = f"https://adventofcode.com/2024/day/{d}/input"
# Get cookie from environment variables
cookie = os.getenv("AOC_SESSION")

# Get the input file and save it
req = urllib.request.Request(url, headers={'Cookie': cookie})
with urllib.request.urlopen(req) as response:
    with open(f"day{d}.input.txt", 'wb') as f:
        f.write((response.read()).strip())

# Create the template file
filename = f"day{d}.py"
template = f"with open('day{d}.input.txt', 'r') as f:\n\n# Part 1\n\nprint(\"Total 1: \")\n\n# Part 2\n\nprint(\"Total 2: \")"
with open(filename, 'w') as f:
    f.write(template)