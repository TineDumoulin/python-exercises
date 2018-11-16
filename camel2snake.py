def camel_2_snake(s):
    '''Converts a CamelCaseString (s) into a snake_case_string.
    s: str, string you want converted from camel into snake case.'''
    
    import re
    pattern = r'[A-Z][^A-Z]*'
    
    words = re.findall(pattern, s)
    snake = '_'.join(words)
    lowersnake = snake.lower()
    
    return lowersnake

camel_2_snake('TurnThisIntoASnakeCaseString')