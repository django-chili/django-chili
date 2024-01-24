Template Tags
=============

{% bowl %}
----------

*Usage:*

.. code-block:: django

    {% bowl path %}
    {% endbowl %}

Loads HTML from a file for use by child tags (between bowl and endbowl).

.. list-table:: Tag Arguments

   * - **path**
     - Path to a static HTML file relative to your Django site root.



{% chop %}
----------

*Usage:*

.. code-block:: django

    {% chop "selector" target="tag|inner|attr" attr="" %}
    {% endchop %}

Finds one or more elements and applies the specified updates to
each. The rendered child content will be applied to the target.

.. list-table:: Tag Arguments

    *   - **selector**
        - CSS selection expression (similar to jQuery).
    *   - **target**
        - Can be either of these values:
            -   **tag** *(default)*: will replace the entire tag.
            -   **inner**: will replace the children of the tag.
            -   **attr**: will insert or replace the tag attribute. If used, then the **attr** argument (below)
                is required.
    *   - **attr** *(optional)*
        - The name of the elements' attribute to add/replace. Required when **target** is **attr**.



{% chunk %}
-----------

*Usage:*

.. code-block:: django

    {% chunk %}

Emits the current value of the selected tag in-place, to be rendered as part of the entire **chop** body.
