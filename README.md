# BeautifulPrint
This module can colorizing any text in your terminal

# Quick start

## Hello world
This is a simple hello world:
```python
from BeautifulPrint import *

bprint("Hello world!", 
       FORMATTING.BOLD, 
       FOREGROUND.RED, 
       BACKGROUND.GREEN)
```
In your console you can see something like this:

<img src="/mdcontent/src1.png"/>

## Unreadable symbols
If you see incomprehensible symbols instead of colors in the console, perform this function at the beginning of your code:
```python
from BeautifulPrint import *
neutralizeColorProblem()
```

## Templates
In this module you can use some templates for beautiful print on terminal:

```python
from BeautifulPrint import *

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

<img src="/mdcontent/src2.png"/>