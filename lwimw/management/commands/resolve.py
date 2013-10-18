from django.core.management.base import BaseCommand, CommandError
from game.models import *
import random

class Command(BaseCommand):
    args = ''
    help = 'Run this command whenever the turn is over.'

    def handle(self, *args, **options):
        day_setting = Setting.objects.get(name='Current Day')
        day_setting.value = str(int(day_setting.value) + 1)
        day_setting.save()

        print 'Generating new units'
        self.generate_units_from_resources()

        #print 'Attacking walls'
        #self.attack_walls()

        print 'Resolving battles'
        self.resolve_battles()

        print 'Assigning squares\' ownership'
        self.assign_squares_ownership()

        print 'Reticulating splines'

        print 'ALL DONE'

    def generate_units_from_resources(self):
        for square in Square.objects.all():

            # If the square is owned and has a resource, we will be generating a unit
            if square.resource_amount > 0 and square.owner != None:
                found = False
                for unit in square.units.all():
                    if unit.owner == square.owner:
                        square.resource_amount -= 1
                        # If there's a battle going on, place the unit on the square
                        if square.units.count() > 1:
                            unit.amount += 1
                            unit.save()
                        # Otherwise just put the unit into the unplaced units
                        else:
                            square.owner.unplaced_units += 1
                            square.owner.save()

                        square.save()
                        found = True
                        break
                if not found:
                    # There are no units on the square, so add a new one
                    square.owner.unplaced_units += 1
                    square.owner.save()
                    square.resource_amount -= 1
                    square.save()

    def resolve_battles(self):
        for square in Square.objects.all():
            units_list = list(square.units.all())
            while square.units.count() > 1:

                loser = random.choice(units_list)
                loser.amount -= 1
                if loser.amount == 0:
                    loser.delete()

            for unit in units_list:
                unit.save()

            # TODO make it so you can tell how many units each player lost

            #print 'On square (%d, %d), ' % (square.col, square.row),
            #for i, unit in enumerate(square.units.all()):
            #    if unit != winning_unit:
            #        print '%s loses (%d units, %.3f) ' % (unit.owner.leader_name, unit.amount, battle_scores[i]),
            #        unit.amount -= 1
            #        if unit.amount == 0:
            #            unit.delete()
            #            print
            #        else:
            #            unit.save()
            #    else:
            #        print '%s wins (%d units, %.3f) ' % (winning_unit.owner.leader_name, winning_unit.amount, battle_scores[winner_idx]),
            #print


    def assign_squares_ownership(self):
        for square in Square.objects.all():
            if square.units.count() == 1:
                square.owner = square.units.all()[0].owner
                square.save()
