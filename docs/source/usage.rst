Usage
*****

Installation
============

To use Django Chili, first install it using pip:

.. code-block:: console

    (.venv) $ pip install django-chili

Configuration
=============

Add the following to your Django ``settings.py`` file:

.. code-block:: python

    TEMPLATES = [
        {
            'OPTIONS': {
                ...
                'libraries': {
                    ...
                    'django_chili': 'django_chili',
                },
            },
        },
    ]

Example
=======

Django Chili operates by loading HTML into an in-memory DOM (Beautiful Soup instance), locating elements using
CSS selectors, applying Django template tags to modify them (replacing either all or part of the matched elements),
and ultimately returning the final result to Django.

It serves as an effective method for creating base templates that can be extended using static HTML files,
eliminating the need for direct updates with Django tags.

.. code-block:: django

    {% load django_chili %}

    {% bowl static/frame.html %}

        {% chop 'title' %}<title></title>{% endchop %}

        {% chop 'div#content' %}
            {% block content %}{% endblock %}
        {% endchop %}

        {% chop 'a#home', target='attr', attr='href' %}{% url 'home' %}{% endchop %}
        {% chop 'a#signup', target='attr', attr='href' %}{% url 'account_signup' %}{% endchop %}

        {% chop '#username' %}{{ user.username }}{% endchop %}
        {% chop 'img#gravatar', target='attr', attr='src' %}{% gravatar_url user.email 32 %}{% endchop %}

        {% chop '.if_authenticated' %}
            {% if user.is_authenticated %}
                {% chunk %}
            {% endif %}
        {% endchop %}

    {% endbowl %}

Breakdown
---------

Let's look at the example below and break it down to understand more:

#.  **load** loads django-chili so we can use the tags it provides.
#.  **bowl** loads an HTML file and uses it until the `{% endbowl %}` tag is found.
#.  **chop** finds elements within the HTML file using CSS selection, then either replaces the entire tag,
    the inner portion of the tag, or just one attribute of the tag.
#.  **chunk** will emit the tag found, allowing you to wrap tags with content.


See :doc:`/reference/templatetags` for details on the options available with each tag.
