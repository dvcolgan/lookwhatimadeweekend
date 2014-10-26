from django.test import TestCase
from lwimw.tests.factories import (
    ContestFactory,
    SubmissionFactory,
    RatingFactory)
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ContestTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_contest_state(self):
        """
        Ensures that the get_contest_state method returns the correct value for
        some specific dates.
        """
        contest = ContestFactory()
        self.assertEquals(
            contest.get_contest_state(contest.start - relativedelta(hours=1)),
            'before')

        self.assertEquals(
            contest.get_contest_state(contest.start + relativedelta(hours=1)),
            'during')

        self.assertEquals(
            contest.get_contest_state(contest.start + relativedelta(
                hours=48, minutes=30)),
            'submitting')

        self.assertEquals(
            contest.get_contest_state(contest.start + relativedelta(hours=50)),
            'judging')

        self.assertEquals(
            contest.get_contest_state(contest.start + relativedelta(weeks=3)),
            'after')

    def test_get_results(self):
        """
        Ensures that get_results returns a list of annotated submissions,
        sorted by their ratings.
        """
        contest = ContestFactory()

        submission0 = SubmissionFactory(
            title="A Poorly Made Program", contest=contest)
        RatingFactory(submission=submission0)
        RatingFactory(
            submission=submission0,
            innovation=1,
            refinement=1,
            artistry=1,
            overall=1)

        submission1 = SubmissionFactory(
            title="Guess What - A Text Adventure!", contest=contest)
        RatingFactory(submission=submission1)
        RatingFactory(
            submission=submission1,
            innovation=5,
            refinement=5,
            artistry=5,
            overall=5)

        results = contest.get_results()
        self.assertEquals(results[0].pk, submission1.pk)
        self.assertEquals(results[0].avg_overall, 4)
        self.assertEquals(results[1].pk, submission0.pk)
        self.assertEquals(results[1].avg_overall, 2)
