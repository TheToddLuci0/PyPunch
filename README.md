# PyPunch
### Python Punch Card Maker
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=TheToddLuci0_PyPunch&metric=alert_status)](https://sonarcloud.io/dashboard?id=TheToddLuci0_PyPunch)
[![PyPI version fury.io](https://badge.fury.io/py/PyPunch.svg)](https://pypi.python.org/pypi/PyPunch/)
[![GitHub license](https://img.shields.io/github/license/TheToddLuci0/PyPunch.svg)](https://github.com/TheToddLuci0/PyPunch/blob/master/LICENSE)


## Overview
This package creates a simple graphical representation of an old IBM 029 keypunch puchcard.
By default, saves the punch card to `out_card.png`. This can be changed by specifying a different
filepath (see below). It uses Pillow internally, so _most_ image types are supported, depending on
filename extension.


## Usage
The following methods are available: 
<hr>

`PyPunch.build_card(command: str = "Example Command", out_file="out_card.png")`:

This is the main function of this module. Optionally takes a command and a filename, then generates
a punch card with this command, and saves it at `out_file`. 

***NOTE: THIS IS NOT A COMPILER!***
The output of this module is just an encoded string. Compilation is much more complex, and requires
knowledge of the whole program and system architecture, and is therefore left as an exercise for the
reader.
<hr>

`PyPunch.mappings`:

This is a dict consisting of valid characters mapped to a list of the positions that need to be punched 
out of the card. For example, `'I': (0, 11)` indicates that punching I requires a punch in positions 0 
and 11. 
