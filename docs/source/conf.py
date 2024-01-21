from pathlib import Path

project = 'Django Chili'
copyright = "2024, Sean O'Dell"
author = 'seanodell'

v = (Path(__file__).parent / '../../VERSION').resolve().read_text().split('.')

release = f"{v[0]}.{v[1]}"
version = f"{v[0]}.{v[1]}.{v[2]}"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'

epub_show_urls = 'footnote'
