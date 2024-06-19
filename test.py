import pyautogui
import time
import keyboard

FILE = "script.txt"
script = open(FILE, "r")
print("t minus")

count = 5
while count != 0:
    print(count)
    time.sleep(1)
    count -= 1

print("YYAYY")

for i in script:
    line = script.readline()
    pyautogui.typewrite(line + i + '\n')
    #because its too flippin fast
    time.sleep(0.5)
    # failsafe :)
    if keyboard.is_pressed('q'):
        break

script.close()
