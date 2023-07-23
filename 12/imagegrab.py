from PIL import ImageGrab, Image, ImageShow
import time
import os
import pyautogui 


# PATH = 'D:\\screenshot256'
# file = os.path.join(PATH)
# time.sleep(3)
# # s = time.time()
# for i in range(100):
#     screenshot = ImageGrab.grab(bbox=(330,280,950,500)).resize((124,44)).convert('L') ##width: 620px , height: 220px 
# # # # ImageShow.show(screenshot)
#     screenshot.save(f'{file}/image{str(i)}.png')
# # # #     data = screenshot.load()
# # e = time.time()
# # print(e-s)



my_img = Image.open('D:\screenshot256\image8.png')

data = my_img.load()

#cactus
sum_gray_pixel = 0
s = time.time()
for w in range(11,26): #w = 95
    for h in range(24,29):
        sum_gray_pixel += data[w,h]
        data[w,h] = 0
        
# e = time.time()
# print(e-s) 

print(f'how much is with? {sum_gray_pixel}')
my_img.show()

# if sum_gray_pixel < 741000:
#     pyautogui.press('space')


#middle rectangle
# def middle_rectangle():
#     sum_gray_pixel=0
#     for w in range(170,280):
#         for h in range(120,150):
#             sum_gray_pixel += data[w,h]
#             return sum_gray_pixel 

