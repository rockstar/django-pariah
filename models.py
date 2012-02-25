from django.db import models
from django.utils.translation import ugettext as _

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
