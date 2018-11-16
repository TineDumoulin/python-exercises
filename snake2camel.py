def Snake2Camel(string):
    '''Converts a snake-cased string 'string' into camel case.
    string: str, string you want to convert from snake to camel case.'''
    
    spl_string = ' '.join((string.split('_')))
    cap_string = spl_string.title()
    camel_string = ''.join(cap_string.split(' '))
    return camel_string
    
Snake2Camel('snake_to_camel')