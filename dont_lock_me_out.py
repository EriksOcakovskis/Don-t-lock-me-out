#   Don't lock me out. Simulates mouse movement, prevents Windows user form
#   being locked out.
#   Copyright (C) 2016 Eriks Ocakovskis

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

#   Version 1.0.0
#   e-mail: eriks.ocakovskis@gmail.com

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
