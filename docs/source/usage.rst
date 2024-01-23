Usage
=====

Installation
------------

To use Django Chili, first install it using pip:

.. code-block:: console

    (.venv) $ pip install django-chili

Configuration
-------------

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
