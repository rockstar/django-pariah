from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase

from pariah import models


class ComicModelTest(TestCase):
    '''Test for the Comic model.'''

    def test_slugify(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        user = User()
        user.save()

        comic = models.Comic()
        comic.owner = user
        comic.title = title
        comic.save()

        self.assertEqual(comic.slug, slug)

    def test_slugify_not_update(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        user = User()
        user.save()

        comic = models.Comic()
        comic.owner = user
        comic.title = title
        comic.save()

        comic.title = 'Even better name for a test comic'
        comic.save()

        self.assertEqual(comic.slug, slug)
