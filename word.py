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

class Word():

    #Note that pos_in_word is the index of the letter that should be typed, not the letter last typed

    def __init__(self,value,x,y):
        self.word = value
        self.pos_in_word = 0
        self.fully_typed = False

    def letter_typed(self,n):
        #First we must check if the letter typed was the correct letter
        if(n==word[pos_in_word]):
            #The letter was correct, move on to the next one
            pos_in_word = pos_in_word + 1
        else:
            #A mistake was made, reset the position back to the start
            pos_in_word = 0
        #Next we check if the letter we typed was the last one
        if(pos_in_word==word.length()):
            #We hit the end of the word
            fully_typed = true

    def portion_typed(self):
        if((pos_in_word >= word.length()) or (pos_in_word < 0)):
            return "Error encountered"

        return (word[:pos_in_word],word[pos_in_word:])


