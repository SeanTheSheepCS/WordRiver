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
import dictionary
import threading
import word
import screen
import stats
import datetime
import random
import curses
import debug

class Manager():

    def new_game(self):
        '''
            starts a new game
            by choosing random words to be displayed on scr
        '''
        for i in range(self.wordsOnScreen):
            w = self.wordDictionary.pick_word()
            x = 1
            y = random.choice(self.poss_vals)
            self.poss_vals.remove(y)
            self.words.append(word.Word(w,x,y))

        self.scrn.render_title()
        self.game_loop()

    def __init__(self):
        self.prevKey = ''
        self.should_keep_going = True
        self.paused = False
        self.hp = 30
        self.wordDictionary = dictionary.Dictionary("dictionary_testfile")
        self.stat = stats.Stats()
        self.scrn = screen.Screen(self.stat)
        self.scrn.scr.nodelay(1)
        self.words = []
        self.wordsOnScreen = 10
        self.pos_in_word = 0
        self.last_time = datetime.datetime.now()
        self.probableWords = []
        self.poss_vals = list(range(1,self.scrn.height-10))
        self.new_game()

    def restart(self):
        new_game()

    def pause(self, key_pressed):
        #pause menu
        if key_pressed == 27:
            if self.paused:
                self.scrn.unrender_pause()
            else:
                self.scrn.render_pause()

            self.paused = not self.paused
            key_pressed = -1
        elif self.paused:
            self.scrn.scr.addstr(0,0,"PAUSE")
            self.scrn.render_pause()
            if key_pressed == 27:
                self.paused = not self.paused
            elif key_pressed == ord('q'):
                self.should_keep_going = False

    def game_mode(self, key_pressed):
        if self.pos_in_word == 0 and (key_pressed != curses.KEY_ENTER or key_pressed != curses.KEY_SPACE):
        #if first letter typed try to find a word
            self.probableWords = []
            for wor in self.words:
                if wor.word[self.pos_in_word] == key_pressed:
                    self.probableWords.append(wor)
        elif key_pressed != curses.KEY_ENTER or key_pressed != curses.KEY_SPACE:
        #if not first letter
            for wor in self.probableWords:
                if wor.word[self.pos_in_word] != key_pressed:
                    del self.probableWords[self.pos_in_word]
                elif wor.word[self.pos_in_word] == key_pressed and self.pos_in_word == len(word):
                    #If last letter matches the end of the word
                    self.pos_in_word = -1
                    self.stats.score += 1
                    self.poss_vals.append(word.y)
                    self.wordsOnScreen = self.wordsOnScreen - 1
                    self.words.remove(wor)
        elif key_pressed == curses.KEY_ENTER or key_pressed == curses.KEY_SPACE:
            self.pos_in_word = -1

        self.pos_in_word += 1

    def process_input(self):
        key_pressed = self.scrn.scr.getch()
        if key_pressed != -1 and key_pressed != self.prevKey:
            self.prevKey = key_pressed #ESC = 27
        return key_pressed

    def add_words(self):
        '''
            add words to scr if not enough are there
        '''
        if len(self.words) < self.wordsOnScreen:
            w = self.wordDictionary.pick_word()
            y = random.choice(self.poss_vals)
            self.poss_vals.remove(y)
            w = word.Word(w,1,y)
            self.words.append(w)

    def remove_words_out_of_bounds(self):
        for wor in self.words:
            if wor.x+len(wor.word) > self.scrn.width - 3:
                self.stat.missedWords += 1
                self.hp -= 1
                self.poss_vals.append(wor.y)
                self.words.remove(wor)
                empty = word.Word(' ' * len(wor.word), wor.x, wor.y)
                self.scrn.render_word(empty)

    def game_loop(self):
        while self.hp > 0:
            if (not self.paused):

                #push the words along
                new_time = datetime.datetime.now()
                micro_seconds_passed = (new_time-self.last_time).microseconds
                #move the words if enough time has passed

                for wor in self.words:
                    empty = word.Word(' ' * len(wor.word), wor.x, wor.y)
                    self.scrn.render_word(empty)

                if micro_seconds_passed >= (0.1)*(1000000):
                    self.last_time = new_time
                    for wor in self.words:
                        wor.x += self.stat.modifier
                #render words
                for wor in self.words:
                    self.scrn.render_word(wor)
                #self.scrn.render_stats()
                self.scrn.scr.refresh()

            #take in input
            key_pressed = self.process_input()

            #call whatever uses keypressed
            self.pause(key_pressed)
            self.game_mode(key_pressed)
            if (not self.should_keep_going):
                break

            #update data
            self.remove_words_out_of_bounds()
            self.add_words()

        return self.stat
