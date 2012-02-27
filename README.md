django-pariah - A Django app for web comics
===========================================

Installation
------------

To install ``pip install django-pariah``

Usage
-----

In your urls.py, add the following:

    import pariah.urls

    urlpatterns = patterns('',
        url(r'^comics/', include(pariah.urls)),
    )

There are two templates that will need to be created. Here are some sample
templates.

**pariah/comic_detail.html**

    <div>
        <h1>{{comic.title}}</h1>
        <img src="{{comic.image_url}}">
        <div>
            <a href="{{first.get_absolute_url}}">First</a>
        {% if prev %}
            <a href="{{prev.get_absolute_url}}">Previous</a>
        {% endif %}
        {% if next %}
            <a href="{{next.get_absolute_url}}">Next</a>
        {% endif %}
            <a href="{{last.get_absolute_url}}">Last</a>
        <div>
    </div>

**pariah/comic_list.html**

    <ul>
    {% for comic in comics %}
        <li><a href="{{comic.get_absolute_url}}">{{comic.title}}</a></li>
    {% endfor %}
    </ul>

