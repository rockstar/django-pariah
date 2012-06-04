from datetime import datetime

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


class ComicPostModelTest(TestCase):
    '''Test for the ComicPost model.'''

    def setUp(self):
        self.user = User()
        self.user.save()

        self.comic = models.Comic()
        self.comic.owner = self.user
        self.comic.title = 'Test comic'
        self.comic.save()

    def test_save_slug(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        post = models.ComicPost()
        post.title = title
        post.comic = self.comic
        post.published = datetime.now()
        post.save()

        self.assertEqual(post.slug, slug)
