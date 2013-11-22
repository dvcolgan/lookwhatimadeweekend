from django.test import Client, TestCase
from django.contrib.auth import authenticate, login
from lwimw.models import *
from django.utils import simplejson
from nose.tools import *
from datetime import date

import ipdb


class TestContestModel(TestCase):

    def test_get_contest_state(self):
        contest = Contest(
            number=1,
            theme='Next Gen Colour-Changing GUI',
            month=6,
            year=2000
        )

        assert_equal(contest.get_contest_state(date(2000, 1, 1)),  'before', 'Way before')
        assert_equal(contest.get_contest_state(date(2000, 5, 1)),  'before', 'A month before')
        assert_equal(contest.get_contest_state(date(2000, 6, 1)),  'during', 'During')
        assert_equal(contest.get_contest_state(date(2000, 7, 1)), 'judging', 'Judging')
        assert_equal(contest.get_contest_state(date(2000, 8, 1)),   'after', 'After')
        assert_equal(contest.get_contest_state(date(2000, 12,1)),   'after', 'Way after')
