# PaintPrint
This module can colorize any text in your terminal

[![Downloads](https://static.pepy.tech/personalized-badge/paintprint?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/paintprint)
[![Downloads](https://static.pepy.tech/personalized-badge/paintprint?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month)](https://pepy.tech/project/paintprint)
[![Downloads](https://static.pepy.tech/personalized-badge/paintprint?period=week&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week)](https://pepy.tech/project/paintprint)
[![Supported Versions](https://img.shields.io/pypi/pyversions/PaintPrint)](https://pypi.org/project/paintprint)
[![Version](https://img.shields.io/pypi/v/PaintPrint)](https://pypi.org/project/paintprint)
[![](https://img.shields.io/pypi/format/PaintPrint)](https://pypi.org/project/paintprint)
[![](https://img.shields.io/pypi/wheel/PaintPrint)](https://pypi.org/project/paintprint)


[![github](https://img.shields.io/badge/-git%20hub-black?style=for-the-badge&logo=github)](https://github.com/tankalxat34/PaintPrint)
[![PyPi](https://img.shields.io/badge/-pypi-006DAD?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/paintprint)

[![GitHub Repo stars](https://img.shields.io/github/stars/tankalxat34/PaintPrint?style=social)](https://github.com/tankalxat34/PaintPrint)

**Author: [tankalxat34](mailto:tankalxat34@gmail.com?subject=User%20of%20PaintPrint)**

# Installing
```bat
pip install PaintPrint
```

# Quick start

## Hello world
This is a simple hello world:
```python
from PaintPrint import *

bprint("Hello world!", 
       FORMATTING.BOLD, 
       FOREGROUND.RED, 
       BACKGROUND.GREEN)
```
In your console you can see something like this:

<img src="https://sun9-51.userapi.com/impg/IT0eADkdwaa9P-ioqdvS5odxwRDkMQovT0Wflw/issddN7LQOs.jpg?size=1009x432&quality=96&sign=9ef43db819f6b795dea2736da8856808&type=album"/>

## Unreadable symbols
If you see incomprehensible symbols instead of colors in the console, perform this function at the beginning of your code:
```python
from PaintPrint import *
neutralizeColorProblem()
```

## Templates
In this module you can use some templates for beautiful print on terminal:

```python
from PaintPrint import *

bprint("TEMPLATES", 
       FORMATTING.BORDERED, 
       FORMATTING.BOLD, 
       FOREGROUND.MAGENTA, 
       BACKGROUND.WHITE)

print("Template for links: " + bformat("python.org", TEMPLATE.URL))
bprint("This is a `positive` template", TEMPLATE.POSITIVE)
bprint("\tAnd this is a `negative`", TEMPLATE.NEGATIVE)
print("You also can write " + bformat("yes", TEMPLATE.YES) + " and " + bformat("no", TEMPLATE.NO) + " like here")
print("If you like " + bformat("black and white", TEMPLATE.BLACKWHITE1) + " or " + bformat("white and black", TEMPLATE.BLACKWHITE2) + " you can using special templates!")
```

Result:

<img src="https://sun9-32.userapi.com/impg/LannX-z_IBqLVLfRX9wGq2xDy7CihWleznmfkw/M_3K9UTjZGA.jpg?size=1009x432&quality=96&sign=88fb94abe1bb88aa4426fb8cd3b14533&type=album"/>

# All functions
Open [test file](https://github.com/tankalxat34/PaintPrint/blob/main/test_PaintPrint.py) and perform in your PC. You will see something like this:

<img src="https://sun9-37.userapi.com/impg/NWYKY66TbieKB8XnhJmfrUvzwE9DQIeEwKApaQ/IOxQmPAm2Ys.jpg?size=1009x959&quality=96&sign=cd7ce7251d980a6cbbb8cea85c6d42d8&type=album"/>
