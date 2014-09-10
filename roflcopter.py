#!/usr/bin/python

#Copyright [yyyy] [name of copyright owner]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
# ROFLCOPTER !!1!11
# Because why not

import curses
from time import sleep

frames = [
"""                     
 ROFL:ROFL:          
         _^___       
      __/   [] \     
LOL===__        \    
        \________]   
         I   I       
        --------/    
""",
"""                     
          :ROFL:ROFL 
         _^___       
 L    __/   [] \     
 O ===__        \    
 L      \________]   
         I   I       
        --------/    
"""
]

class RoflCopter:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.stdscr.nodelay(1)
        self.win = curses.newwin(24, 80, 0, 0)
    
    def main(self):
        done = False
        i = 0
        while not(done):
            self.win.addstr(0, 0, frames[i], curses.A_STANDOUT)
            self.win.addstr(10, 7, 'ROFL !1!!11!', curses.A_STANDOUT)
            self.win.bkgd(' ', curses.A_STANDOUT)
            self.win.refresh()
            
            if i == 0:
                i = 1
            elif i == 1:
                i = 0
            
            key = self.stdscr.getch()
            if key == ord('q'):
                done = True
            sleep(0.1)

    def stop(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.curs_set(1)
        self.stdscr.nodelay(0)
        curses.endwin()

if __name__ == '__main__':
    rofl = RoflCopter()
    try:
        rofl.main()
        rofl.stop()
    except Exception:
        rofl.stop()
        raise