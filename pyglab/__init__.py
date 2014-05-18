"""
Pyglab
~~~~~~

Pyglab is a wrapper for the GitLab API, written in Python.

:copyright: (c) 2014 Michael Schlottke
:license: MIT (see LICENSE for more details)
"""

__title__ = 'pyglab'
__version__ = '0.2.0dev'
__author__ = 'Michael Schlottke'
__license__ = 'MIT'
__copyright__ = '(c) 2014 Michael Schlottke'

from .pyglab import Pyglab
from .exceptions import RequestError
from .apirequest import ApiRequest, RequestType
