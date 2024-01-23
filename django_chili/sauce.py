from bs4 import BeautifulSoup


class Sauce(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    @classmethod
    def _markup_is_url(cls, markup):
        pass

    @classmethod
    def _markup_resembles_filename(cls, markup):
        pass
