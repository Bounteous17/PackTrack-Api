class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def consoleLog(**args):
    action = args.get('action')
    dsplColor = bcolors.WARNING
    if action == 'success':
        dsplColor = bcolors.OKGREEN
    elif action == 'error':
        dsplColor = bcolors.FAIL
    elif action == 'info':
        dsplColor = bcolors.OKBLUE
    print (dsplColor + args.get('msg') + bcolors.ENDC)
