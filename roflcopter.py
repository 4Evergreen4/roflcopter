#!/usr/bin/python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

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