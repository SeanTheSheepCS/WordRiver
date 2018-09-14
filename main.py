'''
WordRiver typing game.
Copyright (C) 2018 Sean Kenny Vlad C.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License

along with this program. If not, see http://www.gnu.org/licenses/.
'''

import curses
import screen
import stats

def main(stdscr):
    try:
        test()
    except:
        pass 

'''
    testing function allowing to draw and process only parts of the game
'''
def test():
    scr = screen.Screen(stats.Stats())
    scr.render_title()
    scr.scr.refresh()
    while(True):
        pass

if __name__ == "__main__":
    curses.wrapper(main)
