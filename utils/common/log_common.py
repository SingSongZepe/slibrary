from value.strings import sslog

# will not write to log file
# just use to remain the user what to do

def ln_c(msg):
    print(sslog + '[NOR] ' + msg)


def lw_c(msg):
    print(sslog + '[WAR] ' + msg)


def le_c(msg):
    print(sslog + '[ERR] ' + msg)


