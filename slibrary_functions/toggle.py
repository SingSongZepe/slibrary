
from value.strings import *
from value.color import *
from value.value import *

def toggle(self, type):
    if type == self.current_type:
        return
    self.lb_selected[type].setStyleSheet(f'background: {colors_selected[type]}; border-radius: {lb_selected_radius}px;')
    self.lb_selected[self.current_type].setStyleSheet(f'background: {color_basic};')

    self.wgt_mains[type].setVisible(True)
    self.wgt_mains[self.current_type].setVisible(False)

    self.current_type = type

    