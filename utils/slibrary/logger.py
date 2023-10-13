
from value.strings import sslog

def ln(self, msg):
    print(sslog + '[NOR] ' + msg)


def lw(self, msg):
    print(sslog + '[WAR] ' + msg)


def le(self, msg):
    print(sslog + '[ERR] ' + msg)

# log in file and store
# emit a signal
def log_file(self, msg):
    pass

