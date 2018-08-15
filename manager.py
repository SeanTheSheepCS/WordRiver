'''
WordRiver typing game.
Copyright (C) 2018 Sean Vlad C.

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
import word
import screen
import stats
import datetime

class Manager():

    def new_game(self):
        '''
            starts a new game
        '''
        for i in range(wordsOnScreen):
            w = wordDictionary.pick_word()
            x = 0
            y = random.randint(self.scrn.height-10)
            self.words = word.Word(w,x,y)

    def __init__(self):
        self.wordDictionary.import_dictionary()
        self.hp = 10
        self.wordDictionary = Dictionary.Dictionary(test)
        self.stat = stats.Stats()
        self.scrn = screen.Screen(self.stat)
        self.words = []
        self.wordsOnScreen = 10
        self.last_time = datetime.now()
        self.new_game()

    def restart(self):
        new_game()

    def process_input(self):
        pass

    def add_words(self):
        if len(self.words) < self.wordsOnScreen:
            w = self.wordDictionary.pick_word()
            y = random.randint(0,self.scrn.height-10)
            w = word(w,0,y)
        self.words.append(w)

    def game_loop(self):
        while self.hp > 0:
            #render words
            for word in self.words:
                self.scrn.render_word(word)
            self.scrn.render_stats(self.stat)

            #push the words along
            new_time = datetime.now()
            seconds_passed = (new_time-self.last_time).seconds
            if(seconds_passed >= 1):
                for word in self.words:
                    word.x = word.x+(modifier*seconds_passed)
                    word.y = word.y+(modifier*seconds_passed)

            #take in input
            self.process_input()

            #update data
            self.add_words()

        return self.stat
