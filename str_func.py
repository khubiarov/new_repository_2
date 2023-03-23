def str_func(source_string):
    return source_string.upper()

def first_letter(source_string):
    '''get string and return string with first-letter in high register'''
    numb = len(source_string)
    return f'{source_string[0].upper}{source_string[1:numb]}'
