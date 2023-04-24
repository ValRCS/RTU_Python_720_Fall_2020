## Some silly example functions

def text_splitter(text):
    return text.split()

def text_joiner(text_list):
    return " ".join(text_list)

def text_reverser(text):
    return text[::-1]

def text_repeater(text, times):
    return text * times