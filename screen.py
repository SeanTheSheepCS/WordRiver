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

class Screen():

    def __init__(self, stat):
        self.height = 60
        self.width = 80
        self.stats = stat
        self.scr = curses.initscr()
        curses.cbreak()
        self.scr.keypad(True)
        curses.noecho()

    def draw_box(x,y):
        '''
            draws a box from xy to the bottom of the screen
        '''
        for i in range(height-y):
            if i == 0 or i == height-y-1:
                stars = ''.join(['*' for i in range(self.width)])
                self.scr.addstr(i,0,stars)
            else:
                self.scr.addstr(i,0,'*')
                self.scr.addstr(i,self.width-1,'*')

    def clear(self):
        self.scr.clear()
        self.scr.refresh()

    def render_word(self,word):
        scr.addstr(math.floor(word.x),math.floor(word.y),word.word)
        
    def render_stats(self):
        self.draw_box(self.width,self.height-10)

    def uninit(self):
        self.scr.keypad(False)
        curses.echo()
        curses.endwin()
