from django.db import models
from django.core import urlresolvers
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify


#TODO: Make upload_to configurable

class ComicPost(models.Model):
    '''A single comic post.'''

    image = models.ImageField(upload_to='comics')
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(editable=False)

    created = models.DateTimeField(_('Creation time'), auto_now_add=True)
    published = models.DateTimeField(_('Publish time'))
    last_modified = models.DateTimeField(
        _('Last modified time'), auto_now=True)

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
