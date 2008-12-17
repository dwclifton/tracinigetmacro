"""@package IniGetMacro
   @file macro.py
   @brief The IniGetMacro class

   Return the value of a trac.ini [section] option.

   @author Douglas Clifton <dwclifton@gmail.com>
   @date December, 2008
   @verion 0.1
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.wiki.model import WikiPage
from trac.config import Option

class IniGetMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        """return value of a trac.ini [section].option"""
        
        section, option = self.parse(args)
        if self.env.config.has_option(section, option):
            return self.env.config.get(section, option)
        else:
            return system_message('No option %s in section [%s]'%(option, section))
    
    def parse(self, args):
        """return (section option) tuple from parameter string"""
        import re
        try:
            section, option = re.sub('\s+', '', args).split('.', 1)
        except ValueError:
            return system_message('Invalid parameter: "%s"'%args)
        return (section, option)
