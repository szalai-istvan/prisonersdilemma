cooperative = 'cooperative'
hostile = 'hostile'
all = [cooperative, hostile]

def validateChoice(choice):
    if choice not in all:
        raise Exception(f'\'{choice}\' is invalid. Acceptable values are {all}')