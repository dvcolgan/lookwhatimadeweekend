from django.contrib.auth.models import User
from lwimw.models import Contest, Category, Submission, Rating
import factory
from datetime import datetime
import string
import random


def generate_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = "myopic_pundit"
    email = "mpundit@gmail.com"


class RandomUserFactory(UserFactory):
    def __init__(self, *args, **kwargs):
        username = generate_str()
        email = "%s@%s.com" % (generate_str(), generate_str())
        super(RandomUserFactory, self).__init__(*args, **kwargs)


class ContestFactory(factory.DjangoModelFactory):
    class Meta:
        model = Contest

    number = 1
    theme = "Partial Nudity"
    start = datetime(year=2014, month=1, day=1, hour=1, minute=1, second=1)


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Software"
    description = "How many ways could you describe \"software\"? Submissions in this category are carefully arranged sets of algorithmic instructions, designed to be run by hardware components. I suppose that sums it up."


class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Submission

    user = factory.SubFactory(RandomUserFactory)
    contest = factory.SubFactory(ContestFactory)
    title = "Ultra Beer Pong"
    category = factory.SubFactory(CategoryFactory)
    comments = ""
    link_1 = "http://test.com/"
    receive_ratings = True


class RatingFactory(factory.DjangoModelFactory):
    class Meta:
        model = Rating

    rater = factory.SubFactory(RandomUserFactory)
    submission = factory.SubFactory(SubmissionFactory)
    innovation = 3
    refinement = 3
    artistry = 3
    overall = 3
    comments = "I feel a sense of absolute ambivalence."
