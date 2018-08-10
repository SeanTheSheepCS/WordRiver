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

class Manager():
    wordDictionary = Dictionary.Dictionary(test)
    scrn = screen.Screen()
    stat = stats.Stats()
    words = []
    wordsOnScreen = 10

    def new_game(self):
        '''
            starts a new game
        '''
        for i in range(wordsOnScreen):
            w = wordDictionary.pick_word()
            x = random.randint(scrn.width)
            y = 0
            self.words = word.Word(w,x,y)

    def __init__(self):
        self.wordDictionary.import_dictionary()
        self.hp = 10
        self.new_game()

    def restart(self):
        new_game()

    def process_input(self):
        pass

    def game_loop(self):
    
        while self.hp > 0:
            #render words
            self.scrn.clear()
            for word in self.words:
                self.scrn.render_word(word)
            self.scrn.render_stats(self.stat)            

            self.process_input()
            
            #update data        

        return self.stat
    
