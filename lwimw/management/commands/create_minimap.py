from django.core.management.base import BaseCommand, CommandError
from game.models import *
from PIL import Image

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    if lv == 1:
        v = int(value, 16)*17
        return v, v, v
    if lv == 3:
        return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

class Command(BaseCommand):
    args = ''
    help = 'Generate a png file of the visible world using Pillow'

    def handle(self, *args, **options):
        squares = Square.objects.order_by('y', 'x')
        first = squares[0]
        last = squares[squares.count()-1]

        width = abs(last.x - first.x) + 100 # this is off somehow, should not have to add 100 to get it to work
        height = abs(last.y - first.y) + 100

        im = Image.new('RGB', (width, height), 'black')

        color_dict = {}
        for color in COLORS:
            color_dict[color[0]] = (color[1], color[2])

        for square in squares:
            print square.x, square.y
            print (width/2 + square.x, height/2 + square.y)
            if square.color == 'white':
                color = (255, 255, 255)
            else:
                color = hex_to_rgb(color_dict[square.color][1])
            if square.units.count() > 0:
                color = hex_to_rgb(color_dict[square.units.all()[0].color][0])

            im.putpixel((width/2 + square.x, height/2 + square.y), color)

        im.save('static/images/minimap.png', 'PNG')
        #TODO create one image of the background and who owns what square,
        # then another that is transparent that just has the units,
        # in the game flash the units on top of the background
        # also in case there are multiple units on a square, show the one with the most, maybe mark it somehow, maybe make squares larger than one pixel?
