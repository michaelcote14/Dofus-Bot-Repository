import pyautogui
import time

#Best Shortcut keys:
#shift tab: will untab any area you want
#Middle mouse button/end button: will cancel program
#ctrl + enter: run program
#closest side mouse click: will duplicate line
#foreward most side mouse click/delete: will delete line
#alt a: move caret to front of line
#alt ;: move caret to back of line







# Give the python file some time before continuing (3 seconds)
time.sleep(3)

# Mouse Functions
print(pyautogui.size()) #Prints the resolution of your screen
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (x location, y location, seconds (3))
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)
# Click (x coordinate, y coordinate, amount of clicks, seconds of click holding)
pyautogui.click(500, 500, 3, 3, button="left")
# Alternative methods for above
#pyautogui.tripleClick()
#pyautogui.doubleClick()
#pyautogui.leftClick()
#pyautogui.rightClick()

# How to scroll (positive numbers will scroll up, negative numbers will scroll down)
pyautogui.scroll(500)

# How to click your mouse and drag somewhere (mouse down=click, mouse up=release)
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
time.sleep(3)
pyautogui.mouseUp()

# Spiral drawing using pyautogui in painter (not finished)
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    pyautogui.dragRel(0, distance, 1, button-"left")
    pyauto.dragRel(-distance, 0, 1, button="left")

pyautogui.displayMousePosition()
# Below will loop things 10 times
for i in range(10): #for loops are used to replay a loop a specified amount of times

# Below will print mouse coordinates continually, and you can use the keyboard shortcut "alt + tab" to switch back and forth to record data
while True:
    print(pyautogui.position())

#Getting RGB values AND coordinates!
import pyautogui
import time

while 1:
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    print(r,g,b,x,y)

    time.sleep(0.5)

#How to use loops and if statements + breaks
x = 11
print('opening')
while True: #how to make the loop go on an unspecified amount of times
    if x == 10: #must be == instead of just = for some reason
        print('x=10')
    else:
        print('worked')
        break #a break will stop any while, for, or nested loops once reached.

