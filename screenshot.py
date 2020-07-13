import time
import pyautogui


def screenshot():
    name= int(round(time.time() * 1000))
    time.sleep(5)
    img=pyautogui.screenshot('screenshots/'+str(name)+'.png')
    img.show()
    
    
screenshot()

