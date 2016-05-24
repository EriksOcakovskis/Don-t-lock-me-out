# Don't log me out
# Version 0.0.2

import sys
import time
import win32api
from threading import Thread

def main_loop():
  while True:
    next_call = time.time()

    current = win32api.GetCursorPos()
    cx = int(current[0]) + 1
    cy = current[1]

    win32api.SetCursorPos((int(cx),int(cy)))

    next_call = next_call + 298;
    if (next_call - time.time()) <= 0:
      time.sleep(10)
    else:
      time.sleep(next_call - time.time())

if __name__ == "__main__":
  print "You will not be locked out."
  print "Close this window when you are done."
  timerThread = Thread(target=main_loop)
  timerThread.start()
