ttf-opensans
=============

.. |py| image:: https://img.shields.io/pypi/pyversions/ttf-opensans.svg

.. |license| image:: https://img.shields.io/pypi/l/ttf-opensans.svg
  :target: https://github.com/Gorialis/ttf-opensans/blob/main/LICENSE

.. |status| image:: https://img.shields.io/pypi/status/ttf-opensans.svg
  :target: https://pypi.python.org/pypi/ttf-opensans

|py| |license| |status|

ttf-opensans is a Python package vending the `Open Sans font by Steve Matteson <https://fonts.google.com/specimen/Open+Sans>`__.

It is intended for when you want to use the Open Sans font family without having to worry about availability on the target system.

The Open Sans font family and this package is licensed under the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__.

Installation
-------------

This package can be installed through the following command:

.. code:: sh

    python3 -m pip install -U ttf-opensans

Usage
------

The fonts are provided through instances of the ``TTFFont`` class.

You can either access a specific font style directly:

.. code:: python3

    import ttf_opensans

    my_font = ttf_opensans.OPENSANS_SEMIBOLDITALIC

Or you can use the helper function to find the most appropriate font style:

.. code:: python3

    from ttf_opensans import opensans

    my_font = opensans(font_weight=600, italic=True)

Once you have the font you want, you can access various attributes on it:

.. code:: python3

    print(my_font.name)  # "OpenSans-SemiBoldItalic"
    print(my_font.weight)  # 600
    print(my_font.italic)  # True
    print(my_font.path)  # pathlib.Path("<...>/site_packages/ttf_opensans/ttf/OpenSans-SemiBoldItalic.ttf")

You can also open the font for reading directly:

.. code:: python3

    with my_font.open() as fp:
        font_data = fp.read()

If you use the Python Imaging Library (Pillow), you can also directly get an ImageFont instance:

.. code:: python3

    from PIL import Image, ImageDraw, ImageFont

    with Image.new("RGB", (512, 512), (255, 255, 255)) as im:
        draw = ImageDraw.Draw(im)
        imagefont = my_font.imagefont(size=48)

        draw.text(font=imagefont, fill=(0, 0, 0), xy=(0, 0), text="Hello World!")
