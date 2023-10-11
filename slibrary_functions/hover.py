# this file use to indicate tab hover

from value.strings import *
from value.color import *

def hover(self, type):
    if self.current_type == type:
        return
    self.lb_selected[type].setStyleSheet(f'''background: {colors_hover[type]};
        border-radius: 3px;''')

def hover_out(self, type):
    if self.current_type == type:
        return
    self.lb_selected[type].setStyleSheet(f'background: {color_basic};')

