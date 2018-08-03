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

import random

class Dictionary():
    '''
        Stores words which will appear in the game
    '''

    def __init__(self, name):
        '''
            name of the dictionary file, where words split by spaces or new lines
            words stores all the words from file
        '''
        self.name = name
        self.words = []
        self.import_dictionary()

    def import_dictionary(self):
        '''
            Import a dictionary must be .txt
        '''
        with open(self.name+".txt", 'r') as f:
            s = f.read()
            self.words = s.split()

    def pick_word(self):
        '''
            Chooses a random word from the list
        '''
        index = random.randrange(0,len(self.words))
        return self.words[index]
