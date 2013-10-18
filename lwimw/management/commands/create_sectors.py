from django.core.management.base import BaseCommand, CommandError
from game.models import *

class Command(BaseCommand):
    args = '<world_width> <world_height>'
    help = 'Create all of the squares in the database.'

    def handle(self, *args, **options):
        world_width = int(args[0])
        world_height = int(args[1])
        world_width / 2

        Setting.objects.all().delete()
        Setting.objects.create(name='world_width', value=world_width)
        Setting.objects.create(name='world_height', value=world_height)

        print 'Added settings to the database'

        print 'Beginning creation of squares'

        Square.objects.all().delete()

        batch = []
        cur = 0
        batch_max = 10000
        total = world_width * world_height


        for x in range(-world_width/2, world_width/2):
            for y in range(-world_height/2, world_height/2):
                batch.append(Square(x=x, y=y))
                if len(batch) > batch_max:
                    Square.objects.bulk_create(batch)
                    cur += batch_max
                    batch = []
                    print 'Created %d of %d squares' % (cur, total)
        print 'Done'
