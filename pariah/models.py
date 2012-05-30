from django.db import models
from django.core import urlresolvers
from django.utils.translation import ugettext as _
from django.conf import settings
from django.template.defaultfilters import slugify


try:
    UPLOAD_TO = settings.PARIAH_UPLOAD_TO
except AttributeError:
    UPLOAD_TO = 'comics'

class Comic(models.Model):
    '''A collection of web comics.'''

    owner = models.ForeignKey('auth.User')

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    description = models.CharField(max_length=300)

    created = models.DateTimeField(_('Creation time'), auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Comic, self).save(*args, **kwargs)

    #TODO: Add format info, tags, etc.


class ComicPost(models.Model):
    '''A single comic post.'''

    image = models.ImageField(upload_to=UPLOAD_TO)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, editable=False)

    comic = models.ForeignKey('Comic')

    created = models.DateTimeField(_('Creation time'), auto_now_add=True)
    published = models.DateTimeField(_('Publish time'))
    last_modified = models.DateTimeField(
        _('Last modified time'), auto_now=True)

    @property
    def image_url(self):
        return '%(MEDIA_URL)s%(image)s' % {
            'MEDIA_URL': settings.MEDIA_URL,
            'image': self.image
            }

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ComicPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return urlresolvers.reverse('comic-detail', kwargs={
            'year': self.published.year,
            'month': self.published.month,
            'day': self.published.day,
            'slug': self.slug })
