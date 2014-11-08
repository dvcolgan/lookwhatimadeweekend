from unittest import TestCase
from lwimw.models import *
from django.utils import simplejson
import pytz
from dateutil.relativedelta import relativedelta
from factories import UserFactory
from datetime import datetime
from mock import Mock
import ipdb

# 9PM EST is 2PM UTC (during daylight savings time)

class TestContestModel(TestCase):
        
    def test_contest_state_before(self):
        contest_date = datetime(2014, 1, 31, 0, 0, 0, tzinfo=pytz.utc)
        contest = Contest(start=contest_date)
        now = contest_date + relativedelta(seconds=-1)
        self.assertEqual(contest.get_contest_state(now), 'before')

    def test_contest_state_start(self):
        contest_date = datetime(2014, 1, 31, 0, 0, 0, tzinfo=pytz.utc)
        contest = Contest(start=contest_date)
        now = contest_date
        self.assertEqual(contest.get_contest_state(now), 'during')

    def test_contest_state_judging(self):
        contest_date = datetime(2014, 1, 31, 0, 0, 0, tzinfo=pytz.utc)
        contest = Contest(start=contest_date)
        now = contest_date+relativedelta(days=4)
        self.assertEqual(contest.get_contest_state(now), 'judging')

    def test_contest_state_middle_during(self):
        contest_date = datetime(2014, 1, 31, 0, 0, 0, tzinfo=pytz.utc)
        contest = Contest(start=contest_date)
        now = contest_date+relativedelta(weeks=4)
        self.assertEqual(contest.get_contest_state(now), 'after')

    def test_user_can_vote(self):
        user = User(pk=1)
        self.assertEqual(True,user_can_vote(user,[Submission(user=user)]))        
        
    def test_user_can_submit(self):
        contest_date = datetime(2014, 1, 31, 0, 0, 0, tzinfo=pytz.utc)
        contest = Contest(start=contest_date)
        now = contest_date
        self.assertEqual(True,contest.can_submit(now))

