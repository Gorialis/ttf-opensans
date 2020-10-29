# -*- coding: utf-8 -*-

"""
Copyright 2020 Devon (Gorialis) R

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pathlib
import typing

try:
    from PIL import ImageFont
except ImportError:
    ImageFont = None


__all__ = (
    'OPENSANS_BOLD',
    'OPENSANS_BOLDITALIC',
    'OPENSANS_EXTRABOLD',
    'OPENSANS_EXTRABOLDITALIC',
    'OPENSANS_ITALIC',
    'OPENSANS_LIGHT',
    'OPENSANS_LIGHTITALIC',
    'OPENSANS_REGULAR',
    'OPENSANS_SEMIBOLD',
    'OPENSANS_SEMIBOLDITALIC',
    'FONTS',
    'opensans',
)


ROOT = pathlib.Path(__file__).parent
TTF_BIN_FOLDER = ROOT / 'ttf'


class TTFFont:
    """
    Represents a vended TTF font.
    You should generally not instantiate this class yourself.
    """

    def __init__(self, font_name: str, font_weight: int, italicized: bool):
        self.name = font_name
        self.path = (TTF_BIN_FOLDER / font_name).with_suffix('.ttf')
        self.weight = font_weight
        self.italic = italicized

    def __repr__(self) -> str:
        return "<TTFFont {0!r}>".format(self.name)

    def open(self) -> typing.BinaryIO:
        return open(self.path, mode='rb')

    if ImageFont:
        def imagefont(self, size: float = 10, encoding: str = 'unic', layout_engine = None) -> ImageFont.ImageFont:
            return ImageFont.truetype(font=str(self.path), size=size, encoding=encoding, layout_engine=layout_engine)


OPENSANS_BOLD = TTFFont("OpenSans-Bold", 700, False)
OPENSANS_BOLDITALIC = TTFFont("OpenSans-BoldItalic", 700, True)
OPENSANS_EXTRABOLD = TTFFont("OpenSans-ExtraBold", 800, False)
OPENSANS_EXTRABOLDITALIC = TTFFont("OpenSans-ExtraBoldItalic", 800, True)
OPENSANS_ITALIC = TTFFont("OpenSans-Italic", 400, True)
OPENSANS_LIGHT = TTFFont("OpenSans-Light", 300, False)
OPENSANS_LIGHTITALIC = TTFFont("OpenSans-LightItalic", 300, True)
OPENSANS_REGULAR = TTFFont("OpenSans-Regular", 400, False)
OPENSANS_SEMIBOLD = TTFFont("OpenSans-SemiBold", 600, False)
OPENSANS_SEMIBOLDITALIC = TTFFont("OpenSans-SemiBoldItalic", 600, True)

FONTS = (
    OPENSANS_BOLD,
    OPENSANS_BOLDITALIC,
    OPENSANS_EXTRABOLD,
    OPENSANS_EXTRABOLDITALIC,
    OPENSANS_ITALIC,
    OPENSANS_LIGHT,
    OPENSANS_LIGHTITALIC,
    OPENSANS_REGULAR,
    OPENSANS_SEMIBOLD,
    OPENSANS_SEMIBOLDITALIC,
)


def opensans(font_weight: int = 400, italic: bool = False):
    """
    Return a TTFFont that matches the chosen italic setting, with the closest font weight.
    """

    return min(
        filter(lambda f: f.italic == italic, FONTS),
        key=lambda f: (abs(f.weight - font_weight), f.weight < font_weight)
    )
