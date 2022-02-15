# BeautifulPrint
This module can colorizing any text in your terminal

# Installing
```bat
pip install BeautifulPrint
```

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

# All functions

Install `BeautifulPrint` in perform this code on your PC:
```python
from BeautifulPrint import *
neutralizeColorProblem()

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

print("\n")

bprint("COLORS - BACKGROUND",
       FORMATTING.BORDERED,
       FORMATTING.BOLD,
       FOREGROUND.MAGENTA,
       BACKGROUND.WHITE)

print("In " + bformat("BeautifulPrint", TEMPLATE.BLACKWHITE1) + " you can find " + bformat("10", FOREGROUND.GREEN)+ " backgrounds and foregrounds:")
bprint("BACKGROUNDS", FORMATTING.BORDERED)
bprint("Red", BACKGROUND.RED, end="\t")
bprint("Green", BACKGROUND.GREEN)

bprint("Yellow", BACKGROUND.YELLOW, end="\t")
bprint("Blue", BACKGROUND.BLUE)

bprint("Magenta", BACKGROUND.MAGENTA, end="\t")
bprint("Cyan", BACKGROUND.CYAN)

bprint("White", BACKGROUND.WHITE, end="\t")
bprint("Black", BACKGROUND.BLACK)

bprint("Gold", BACKGROUND.GOLD, end="\t")
bprint("Silver", BACKGROUND.SILVER)
bprint("Copper", BACKGROUND.COPPER)

print()

bprint("COLORS - BACKGROUND",
       FORMATTING.BORDERED,
       FORMATTING.BOLD,
       FOREGROUND.MAGENTA,
       BACKGROUND.WHITE)
bprint("Red", FOREGROUND.RED, end="\t")
bprint("Green", FOREGROUND.GREEN)

bprint("Yellow", FOREGROUND.YELLOW, end="\t")
bprint("Blue", FOREGROUND.BLUE)

bprint("Magenta", FOREGROUND.MAGENTA, end="\t")
bprint("Cyan", FOREGROUND.CYAN)

bprint("White", FOREGROUND.WHITE, end="\t")
bprint("Black", FOREGROUND.BLACK)

bprint("Gold", FOREGROUND.GOLD, end="\t")
bprint("Silver", FOREGROUND.SILVER)
bprint("Copper", FOREGROUND.COPPER)

print("\n\nAnd more " + bformat("240", FOREGROUND.GOLD) + " colors with indexes, RGB or HEX support:")
for i in range(256):
    bprint("*", UserColor.BACKGROUND(i).get(), end="")
print()
for i in range(256):
    bprint("*", UserColor.FOREGROUND(i).get(), end="")
print("\n")

print("Also you can set your own color by RGB or HEX:")
bprint("Foreground: ", FORMATTING.BORDERED,
       FORMATTING.BOLD,
       FOREGROUND.MAGENTA,
       BACKGROUND.WHITE)
bprint("\t\tPrint by RGB", UserColor.FOREGROUND((150, 15, 240)).get())
bprint("\t\tPrint by HEX", UserColor.FOREGROUND("#960FF0").get())
bprint("\t\tPrint by HEX without #-symbol", UserColor.FOREGROUND("960FF0").get())

bprint("Background: ", FORMATTING.BORDERED,
       FORMATTING.BOLD,
       FOREGROUND.MAGENTA,
       BACKGROUND.WHITE)
bprint("\t\tPrint by RGB", UserColor.BACKGROUND((150, 15, 240)).get())
bprint("\t\tPrint by HEX", UserColor.BACKGROUND("#960FF0").get())
bprint("\t\tPrint by HEX without #-symbol", UserColor.BACKGROUND("960FF0").get())
```

You will see something like this:

<img src="/mdcontent/srcFULL.png"/>