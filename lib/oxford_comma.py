def oxford_comma(items):
    oxford_sentence = ''



    if len(items) < 2:
        return oxford_sentence + items[0]
    elif len(items) < 3:
        return items[0] + ' and ' + items[1]
    else:
        for item in items:
            if items.index(item) == len(items) - 1:
                oxford_sentence += f'and {item}'
            else:
                oxford_sentence += f'{item}, '
    
        return oxford_sentence

