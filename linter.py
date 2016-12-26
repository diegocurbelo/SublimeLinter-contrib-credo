#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Diego Curbelo
# Copyright (c) 2016 Diego Curbelo
#
# License: MIT
#

"""This module exports the Credo plugin class."""
from SublimeLinter.lint import Linter, util


class Credo(Linter):
    """Provides an interface to credo."""

    syntax = 'elixir'
    cmd = ['mix', 'credo', '--format=oneline', '-a', '--read-from-stdin']
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'^\[(?P<warning>W|C)\].*?:(?P<line>\d*):(?P<col>\d*).(?P<message>.+)$'
    multiline = True
    line_col_base = (1, 1)
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
