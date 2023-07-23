from PIL import ImageGrab
import pyautogui 
import time

# the location of game in my browser is 330 from left 280 from top 950 from bottom and 500 from right
BOX = (330,280,950,500)
time.sleep(2)
pyautogui.press('up')
while True:
    #in possition Box take a screen shot
    screenshot = ImageGrab.grab(bbox=BOX).resize((124,44)).convert('L') ##width: 620px , height: 220px 
    data = screenshot.load()
    sum_gray_pixel = 0
    #made a rectangle in posion (70,150) of box, if there is obstcle in rectangle press up
    for w in range(11,26):
        for h in range(24,29):
            sum_gray_pixel += data[w,h]               
    if sum_gray_pixel < 18400:
        pyautogui.press('up')
      



           

            
                 

    









