def get_percentage(num, digits=None):
    return str(round(num * 100, digits) if digits is not None else int(num * 100)) + "%"
