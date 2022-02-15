"""
********************************
*------------------------------*
*----------PaintPrint----------*
*------------------------------*
********************************
Author: tankalxat34
Description:
    This module can colorize any text in your terminal
Contacts:
    - github: https://github.com/tankalxat34/BeautifulPrint
    - email: mailto:tankalxat34@gmail.com?subject=User%20of%20UploadgramPyAPI
    - telegram: https://t.me/tankalxat34
"""
import os


def neutralizeColorProblem():
    """If you see incomprehensible symbols instead of colors in the console, 
    perform this function at the beginning of your code"""
    os.system("cls")

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


class UserColor:
    class FOREGROUND:
        def __init__(self, color):
            self.index_color = color
            if isinstance(self.index_color, int):
                self.color = '\033[38;5;'+str(self.index_color)+'m'
            elif isinstance(self.index_color, str):
                self.index_color = hex_to_rgb(self.index_color)
                self.color = f'\033[38;2;{self.index_color[0]};{self.index_color[1]};{self.index_color[2]}m'
            else:
                self.color = f'\033[38;2;{self.index_color[0]};{self.index_color[1]};{self.index_color[2]}m'

        def get(self):
            return self.color

    class BACKGROUND:
        def __init__(self, color):
            self.index_color = color
            if isinstance(self.index_color, int):
                self.color = '\033[48;5;' + str(self.index_color) + 'm'
            elif isinstance(self.index_color, str):
                self.index_color = hex_to_rgb(self.index_color)
                self.color = f'\033[48;2;{self.index_color[0]};{self.index_color[1]};{self.index_color[2]}m'
            else:
                self.color = f'\033[48;2;{self.index_color[0]};{self.index_color[1]};{self.index_color[2]}m'

        def get(self):
            return self.color


class FORMATTING(object):
    """Formatting text"""
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    PALE = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    UNDERLINE_DOUBLE = '\033[21m'
    BORDERED = '\033[51m'
    CIRCLED = '\033[52m'
    OVERLINED = '\033[53m'
    BLINK_SLOW = '\033[5m'
    REVERSE = '\033[7m'
    INVISIBLE = '\033[8m'
    CROSSEDOUT = '\033[9m'


class FOREGROUND(object):
    """Constants for foreground"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    GOLD = '\033[38;2;255;215;0m'
    SILVER = '\033[38;2;187;187;187m'
    COPPER = '\033[38;2;184;115;51m'


class BACKGROUND(object):
    """Constants for background"""
    RED = '\033[101m'
    GREEN = '\033[102m'
    YELLOW = '\033[103m'
    BLUE = '\033[104m'
    MAGENTA = '\033[105m'
    CYAN = '\033[106m'
    WHITE = '\033[107m'
    BLACK = '\033[100m'
    GOLD = '\033[48;2;255;215;0m'
    SILVER = '\033[48;2;187;187;187m'
    COPPER = '\033[48;2;184;115;51m'


class TEMPLATE(object):
    """String templates with ANSI escapes for colorizing your text"""
    URL = FOREGROUND.BLUE + FORMATTING.UNDERLINE + FORMATTING.ITALIC
    POSITIVE = FORMATTING.BOLD + FOREGROUND.GREEN
    NEGATIVE = FORMATTING.BOLD + FOREGROUND.RED
    BLACKWHITE1 = FOREGROUND.WHITE + BACKGROUND.BLACK
    BLACKWHITE2 = FOREGROUND.BLACK + BACKGROUND.WHITE
    YES = BACKGROUND.GREEN + FOREGROUND.WHITE + FORMATTING.BOLD + FORMATTING.UNDERLINE
    NO = BACKGROUND.RED + FOREGROUND.WHITE + FORMATTING.BOLD + FORMATTING.UNDERLINE


def bformat(text, *args):
    """Can colorize text in string"""
    user_args = ""
    for arg in args:
        user_args += arg
    return user_args + text + FORMATTING.NORMAL


class bprint:
    def __init__(self, text, *args, doprint=True, end="\n"):
        """Printing text on console
        :param text:        Text, that will be printing on your terminal
        :param doprint:     True, if you want to print text without method self.print()
        :param end:         End symbol for text
        """
        self.text = str(text)
        self.args = ""
        self.end = end
        for arg in args:
            self.args += arg
        if doprint:
            print(self.args + self.text + FORMATTING.NORMAL, end=self.end)

    def print(self):
        """printing your colorized text"""
        return print(self.args + self.text + FORMATTING.NORMAL, end=self.end)

    def get_text(self):
        """
        :return:        String with ANSI escape
        """
        return self.args + self.text + FORMATTING.NORMAL


def binput(text, *args):
    """Colorizing the input"""
    user_args = ""
    for arg in args:
        user_args += arg
    return input(user_args + str(text) + FORMATTING.NORMAL)
