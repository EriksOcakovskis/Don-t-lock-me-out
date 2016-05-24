# Don't lock me out
# Version 0.2.0

import sys
import time
import win32api
import ctypes
from threading import Thread

def console_defaults():
  win32api.SetConsoleTitle("Don't lock me out!")

def user_messages():
  print "You will not be locked out."
  print "Close this window when you are done."

def main_loop():
  while True:
    next_call = time.time()

    ctypes.windll.user32.mouse_event(1,2,0,0,0)

    next_call = next_call + 298;
    if (next_call - time.time()) <= 0:
      time.sleep(10)
    else:
      time.sleep(next_call - time.time())

if __name__ == "__main__":
  console_defaults()
  user_messages()
  timerThread = Thread(target=main_loop)
  timerThread.start()
