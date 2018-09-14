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

class Theme():

    def __init__(self,sideborder,roofborder,floorborder,cornerchar,text_colour,background_colour):
        self.sideborder = sideborder
        self.roofborder = roofborder
        self.floorborder = floorborder
        self.cornerchar = cornerchar
        self.text_colour = text_colour
        self.background_colour = background_colour