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
import theme
import math

class Screen():

    def __init__(self, stat):
        self.chosen_theme = theme.Theme('|','-','-','*',curses.COLOR_BLACK,curses.COLOR_CYAN)
        curses.init_pair(1,self.chosen_theme.text_colour,self.chosen_theme.background_colour)
        self.stats = stat
        self.scr = curses.initscr()
        self.height,self.width = self.scr.getmaxyx()
        curses.cbreak()
        self.scr.keypad(True)
        self.scr.refresh()
        curses.noecho()

    '''reads multiline string from txt file '''
    def parsefile(self, fil):
        tag = []
        with open(fil, 'r') as f:
            for line in f.readlines():
                tag.append(line)
        return tag

    '''
        renders title
    '''
    def render_title(self):
        self.render_background()
        self.draw_box(0,0,self.height-2,self.width-2)
        if(self.height-4 > 25 and self.width-4 > 72):
            riverTitle = self.parsefile("title_display_default.txt")
            centre = (self.width-2)/2
            leftOffset = math.floor(centre - 30)
            yCoord = 3
            for line in riverTitle:
                self.scr.addstr(yCoord,leftOffset,line[:-1],curses.color_pair(1))
                yCoord += 1

    def draw_box(self,x,y):
        '''
            draws a box from xy to the bottom of the screen

            Note:
            I am unsure this function works as intended! I would doublecheck this.
            I have made a function that takes in two points that I am fairly sure works as intended as an alternative to this one.
            -Sean
        '''
        for i in range(self.height-y):
            if i == 0 or i == self.height-y-1:
                stars = ''.join(['*' for i in range(self.width)])
                self.scr.addstr(i,0,stars)
            else:
                self.scr.addstr(i,0,'*')
                self.scr.addstr(i,self.width-1,'*')

    def render_background(self):
        for x in range(0,self.height-1):
            for y in range(0,self.width-1):
                self.scr.addstr(x,y,' ',curses.color_pair(1))

    def draw_box(self,x1,y1,x2,y2):
        '''
            Draws a box with top left corner of (x1,y1) and with bottom right corner of (x2,y2)
        '''
        if(not(x1>self.height or x2>self.height or y1>self.width or y2>self.width or x1<0 or x2<0 or y1<0 or y2<0)):
            for x in range(x1,x2):
                self.scr.addstr(x,y1,self.chosen_theme.sideborder,curses.color_pair(1))
                self.scr.addstr(x,y2,self.chosen_theme.sideborder,curses.color_pair(1))
            for y in range(y1,y2):
                self.scr.addstr(x1,y,self.chosen_theme.roofborder,curses.color_pair(1))
                self.scr.addstr(x2,y,self.chosen_theme.floorborder,curses.color_pair(1))
            self.scr.addstr(x1,y1,self.chosen_theme.cornerchar,curses.color_pair(1))
            self.scr.addstr(x1,y2,self.chosen_theme.cornerchar,curses.color_pair(1))
            self.scr.addstr(x2,y1,self.chosen_theme.cornerchar,curses.color_pair(1))
            self.scr.addstr(x2,y2,self.chosen_theme.cornerchar,curses.color_pair(1))
        else:
            return "Nothing done."

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
