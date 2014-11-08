from django.core.management.base import BaseCommand, CommandError
from lwimw.models import *

class Command(BaseCommand):
    args = ''
    help = 'Generate a png file of the visible world using Pillow'

    def handle(self, *args, **options):
        if current_contest.year != now.year or current_contest.month != now.month:
            next_year = current_contest.year
            next_month = current_contest.month + 1
            if next_month > 12:
                next_year += 1
                next_month = 1

            contests = Contest.objects.order_by('-year', '-month')
            current_contest = Contest.objects.create(
                number=current_contest.number + 1,
                theme='Announced Soon',
                month=next_month,
                year=next_year,
            )
