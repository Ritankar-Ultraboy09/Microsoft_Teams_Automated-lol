import time
import pyautogui
import webbrowser

Time_of_Leaving = input("Please enter your leaving time:-")
Meeting_Link = input("Enter the meeting link to leave at the proper time")
TimeRn = time.strftime("%H:%M:%S")

while (TimeRn != Time_of_Leaving):
    print("Time is there"+ TimeRn)
    TimeRn = time.strftime("%H:%M:%S")
    time.sleep(1)

if (TimeRn == Time_of_Leaving):
    print("It's time to go!")
    webbrowser.open(Meeting_Link)
    time.sleep(12)
    pyautogui.moveTo(1550,97)
    pyautogui.click()
    