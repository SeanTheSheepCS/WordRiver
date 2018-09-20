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

class Manager():

    def new_game(self):
        '''
            starts a new game
            by choosing random words to be displayed on scr
        '''
        for i in range(self.wordsOnScreen):
            w = self.wordDictionary.pick_word()
            x = 0
            y = random.choice(self.poss_vals)
            self.poss_vals.remove(y)
            self.words.append(word.Word(w,x,y))

        self.scrn.render_title()
        self.game_loop()

    def __init__(self):
        self.inputQueue = []
        self.should_keep_going = True
        self.paused = False
        self.hp = 10
        self.wordDictionary = dictionary.Dictionary("dictionary_testfile")
        self.stat = stats.Stats()
        self.scrn = screen.Screen(self.stat)
        self.scrn.scr.nodelay(1)
        self.words = []
        self.wordsOnScreen = 10
        self.pos_in_word = 0
        self.last_time = datetime.datetime.now()
        self.probableWords = []
        self.poss_vals = list(range(0,self.scrn.height-10))
        #t = threading.Thread(self.process_input())
        #t.start()
        self.new_game()

    def restart(self):
        new_game()

    def pause(self, key_pressed):
        #pause menu
        if key_pressed == curses.KEY_EXIT:
            self.scrn.render_pause()
            self.paused = not self.paused
        elif self.paused:
            self.scrn.scr.addstr(0,0,"PAUSE")
            self.scrn.render_pause()
            if key_pressed == curses.KEY_EXIT:
                self.paused = not self.paused
            elif key_pressed == curses.KEY_q:
                raise Exception("Goodye Cruel World")

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
        with open('r.txt', 'a') as f:
            f.write('%s\n'%(key_pressed))
        if key_pressed:
            self.inputQueue.append(key_pressed)

    def add_words(self):
        '''
            add words to scr if not enough are there
        '''
        if len(self.words) < self.wordsOnScreen:
            w = self.wordDictionary.pick_word()
            y = random.choice(poss_vals)
            self.poss_vals.remove(y)
            w = word(w,0,y)
            self.words.append(w)

    def game_loop(self):
        while self.hp > 0:

            #push the words along
            new_time = datetime.datetime.now()
            seconds_passed = (new_time-self.last_time).seconds
            self.last_time = new_time
            #move the words if enough time has passed
            if seconds_passed >= 1:
                for wor in self.words:
                    empty = word.Word(' ' * len(wor.word), wor.x, wor.y)
                    self.scrn.render_word(empty)
                    wor.x = wor.x+(self.stat.modifier*seconds_passed)
            #render words
            for wor in self.words:
                self.scrn.render_word(wor)
            self.scrn.render_stats()
            self.scrn.scr.refresh()

            #take in input
            self.process_input()

            #self.process_input() This is handled by the thread!
            key_pressed = ''
            if self.inputQueue:
                key_pressed = self.inputQueue[0]
                self.inputQueue.pop(0)

            #call whatever uses keypressed
            self.pause(key_pressed)
            self.game_mode(key_pressed)
            if (not self.should_keep_going):
                break

            #update data
            self.add_words()

        return self.stat
