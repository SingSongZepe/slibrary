
from value.strings import *
from value.color import *

def toggle_history(self, type):
    if type == self.current_history_type: # it equal, then do nothing
        return

    self.lb_histories[type].setStyleSheet(f'background: {color_basic_deep}')
    self.lb_histories[self.current_history_type].setStyleSheet(f'background: {color_white}')
    #
    self.wgt_histories[type].setVisible(True)
    self.wgt_histories[self.current_history_type].setVisible(False)

    # setText
    self.lb_history_temp.setText(lb_history_temps[type])

    # change current idx
    self.current_history_type = type
