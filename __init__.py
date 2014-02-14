

def restructured_title(string, title_char):
    underline = title_char * len(string)
    return "{string}\n{underline}".format(string=string, underline=underline)


def make_text_date(date):
    return date.strftime("%A, %B %d")
