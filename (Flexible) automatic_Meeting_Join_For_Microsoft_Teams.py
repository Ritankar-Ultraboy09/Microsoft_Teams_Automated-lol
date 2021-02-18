import time
import webbrowser
import pyautogui

Link_For_Meeting= input("Please put your meeting link here:-")
Time_Of_Join = input("put your time(in 24hr format) of join in  HH:MM:SS- ")
TimeNow = time.strftime("%H:%M:%S")

while (TimeNow != Time_Of_Join):
    print("The time has not come yet" +TimeNow+ "it is close!")
    TimeNow = time.strftime("%H:%M:%S")
    time.sleep(1)

if (TimeNow == Time_Of_Join):
    print("Here we go!!")
    webbrowser.open(Link_For_Meeting)
    time.sleep(12)
    pyautogui.moveTo(1450, 750) 
    pyautogui.click()

#made by Ritankar
