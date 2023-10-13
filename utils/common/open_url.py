
from utils.common.log_common import ln_c, lw_c, le_c

from PySide6.QtGui import QDesktopServices

def open_url(url):
    if QDesktopServices.openUrl(url):
        ln_c(f'open url: {url} successfully')
    else:
        le_c(f'fail to open url: {url}')