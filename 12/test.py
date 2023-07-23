from threading import Thread
import time
def a():
    num = ''
    while True:
        num += 'a'
        time.sleep(1)
        print(num,end='')
        if len(num) == 6:
            break
    return 'yesssssssssssssssssssssssssssss'


def b():
    num = 0
    while True:
        num +=1
        time.sleep(1)
        print(num,end='')
        p1.join()
        if num == 3:
            break

if __name__ == "__main__":
    # creating processes
    p1 = Thread(target=a)
    p2 = Thread(target=b)
    
    p1.start()
    p2.start()
  

  


    

    