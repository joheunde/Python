import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # image_20200601_102030.png

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9키를 누르면 스크린샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행