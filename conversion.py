def checkNone(input):
    if input is None:
        return ''
    else:
        return input

def checkFloat(input):
    if input != '—':
        return float(input)
    else:
        return 0