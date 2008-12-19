""" @package WelcomeMacro
    @file macro.py
    @brief The WelcomeMacro class

    Return a welcome heading with the project name extracted from trac.ini.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.2
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.config import Option
from genshi.builder import tag
import re

__all__ = ['WelcomeMacro']

class WelcomeMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        """Return a welcome heading with the project name extracted from trac.ini."""

        section = 'project'
        option = 'name'
        
        if self.config.has_option(section, option):
            return tag.h1('Welcome to the %s Project' % self.config.get(section,
                                                                        option),
                          id='welcome')
        else:
            return system_message('%s: No option "%s" in section [%s]' % (name,
                                                                          option,
                                                                          section))
