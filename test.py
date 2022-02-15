from BeautifulPrint import *
neutralizeColorProblem()

bprint("TEMPLATES", FORMATTING.BORDERED, FORMATTING.BOLD, FOREGROUND.MAGENTA, BACKGROUND.WHITE)
print("Template for links: " + bformat("python.org", TEMPLATE.URL))
bprint("This is a `positive` template", TEMPLATE.POSITIVE)
bprint("\tAnd this is a `negative`", TEMPLATE.NEGATIVE)
print("You also can write " + bformat("yes", TEMPLATE.YES) + " and " + bformat("no", TEMPLATE.NO) + " like here")
print("If you like " + bformat("black and white", TEMPLATE.BLACKWHITE1) + " or " + bformat("white and black", TEMPLATE.BLACKWHITE2) + " you can using special templates!")
#
# print()
#
# bprint("COLORS", FORMATTING.BORDERED, FORMATTING.BOLD, FOREGROUND.MAGENTA, BACKGROUND.WHITE)

input()