""" @package IniGetMacro
    @file macro.py
    @brief The IniGetMacro class

    Return the value of a trac.ini [section] option.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.1
"""

from re import *
from trac.core import *
from StringIO import StringIO
from trac.wiki import Formatter
from trac.util.html import Markup
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.config import Option

class IniGetMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        """return value of a trac.ini [section].option"""
        
        if args.find('.') == -1:
            return system_message('%s: Invalid parameter: "%s"'%(name, args))

        section, option = re.sub('\s+', '', args).split('.', 1)

        if self.config.has_option(section, option):
            out = StringIO()
            text = self.config.get(section, option)
            Formatter(self.env, formatter.context).format(text, out)
            return Markup(out.getvalue())
        else:
            return system_message('%s: No option "%s" in section [%s]'%(name,
                                                                        option,
                                                                        section))
