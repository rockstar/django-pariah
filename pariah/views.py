from datetime import datetime

from django.views import generic

from pariah import models


class ComicsView(generic.ListView):
    '''Generic view for seeing all `pariah.models.ComicPost` instances.'''

    context_object_name = 'comics'
    queryset = models.ComicPost.objects.order_by('-published').filter(
        published__lt=datetime.now)
    template_name = 'pariah/comic_list.html'


class ComicViewBase(generic.DetailView):
    '''Base class for comic views.'''

    context_object_name = 'comic'
    queryset = models.ComicPost.objects.filter(published__lt=datetime.now)
    template_name = 'pariah/comic_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ComicViewBase, self).get_context_data(*args, **kwargs)
        if context['comic'] is None:
            return context
        comic = context['comic']
        try:
            context['first'] = models.ComicPost.objects.order_by(
                'published').filter(published__lt=datetime.now)[0]
        except IndexError:
            pass
        try:
            context['prev'] = models.ComicPost.objects.order_by(
                '-published').filter(
                    published__lt=comic.published)[0]
        except IndexError:
            pass
        try:
            context['next'] = models.ComicPost.objects.order_by(
                'published').filter(
                    published__lt=datetime.now,
                    published__gt=comic.published)[0]
        except IndexError:
            pass
        try:
            context['last'] = models.ComicPost.objects.order_by(
                '-published').filter(published__lt=datetime.now)[0]
        except IndexError:
            pass
        return context


class ComicIndexView(ComicViewBase):
    '''Generic view for the most recent `pariah.models.ComicPost` instance.'''

    def get_object(self):
        try:
            return models.ComicPost.objects.order_by(
                '-published').filter(published__lt=datetime.now)[0]
        except IndexError:
            return None


class ComicView(ComicViewBase):
    '''Generic view for a single `pariah.models.ComicPost` instance.'''
