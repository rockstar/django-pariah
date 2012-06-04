from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase

from pariah import models


class ComicModelTest(TestCase):
    '''Test for the Comic model.'''

    def setUp(self):
        self.user = User()
        self.user.save()

    def _make_comic(self):
        comic = models.Comic()
        comic.owner = self.user
        return comic

    def test_slugify(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        comic = self._make_comic()
        comic.title = title
        comic.save()

        self.assertEqual(comic.slug, slug)

    def test_slugify_not_update(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        comic = self._make_comic()
        comic.title = title
        comic.save()

        comic.title = 'Even better name for a test comic'
        comic.save()

        self.assertEqual(comic.slug, slug)

    def test_posts_empty(self):
        comic = self._make_comic()
        comic.save()

        self.assertEqual(comic.posts.count(), 0)

    def test_posts(self):
        comic = self._make_comic()
        comic.save()

        post = models.ComicPost()
        post.title = 'First comic'
        post.comic = comic
        post.published = datetime.now() - timedelta(days=2)
        post.save()

        self.assertEqual(comic.posts.count(), 1)


class ComicPostModelTest(TestCase):
    '''Test for the ComicPost model.'''

    def _make_post(self):
        post = models.ComicPost()
        post.title = 'First comic'
        post.comic = self.comic
        post.published = datetime.now() - timedelta(days=2)
        return post

    def setUp(self):
        self.user = User()
        self.user.save()

        self.comic = models.Comic()
        self.comic.owner = self.user
        self.comic.title = 'Test comic'
        self.comic.save()

    def test_next_none(self):
        post = self._make_post()
        post.save()

        self.assertEqual(post.next, None)

    def test_next(self):
        post = self._make_post()
        post.save()

        post2 = models.ComicPost()
        post2.title = 'Second comic'
        post2.comic = self.comic
        post2.published = datetime.now() - timedelta(days=1)
        post2.save()

        self.assertEqual(post.next, post2)

    def test_prev(self):
        post = self._make_post()
        post.save()

        post2 = models.ComicPost()
        post2.title = 'Second comic'
        post2.comic = self.comic
        post2.published = datetime.now() - timedelta(days=1)
        post2.save()

        self.assertEqual(post2.prev, post)

    def test_prev_none(self):
        post = self._make_post()
        post.save()

        self.assertEqual(post.prev, None)

    def test_save_slug(self):
        title = 'Super fun test comic'
        slug = slugify(title)

        post = models.ComicPost()
        post.title = title
        post.comic = self.comic
        post.published = datetime.now()
        post.save()

        self.assertEqual(post.slug, slug)
