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

from dictionary import *

'''
    tests reading from testfile
    and choosing words from it in random order
'''
def dict_test():
    d = Dictionary("dictionary_testfile")
    print(d.words)
    for i in range(10):
        print(d.pick_word())


if __name__ == "__main__":
    dict_test()
