"""@package IniGetMacro
   @file macro.py
   @brief The IniGetMacro class

   Return the value of a trac.ini [section] option.

   @author Douglas Clifton <dwclifton@gmail.com>
   @date December, 2008
   @version 0.11.1
"""

#from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
#from trac.wiki.model import WikiPage
from trac.config import Option
import re

class IniGetMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, param):
        """return value of a trac.ini [section].option"""
        
        if param.find('.') == -1:
            return system_message('%s: Invalid parameter: "%s"'%(name, param))
        section, option = self.parse(param)
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            return system_message('%s: No option "%s" in section [%s]'%(name,
                                                                        option,
                                                                        section))
    def parse(self, param):
        """return (section, option) tuple from parameter string"""
        
        try:
            section, option = re.sub('\s+', '', param).split('.', 1)
        except ValueError:
            return
        return (section, option)

