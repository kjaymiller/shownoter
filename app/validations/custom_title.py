"""Detect Links and Title Using Common Separators"""
separtators = ['-', ' - ', '- ', ' -', ':']


def detect_custom_title(content):
    separated_string = content.split(' - ', 1)

    if len(separated_string) == 2:
        result = {'title': separated_string[0],
                  'url': separated_string[1]}
        return result

    else:
        return None
