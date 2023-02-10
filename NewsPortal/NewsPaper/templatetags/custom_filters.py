import re

from django import template


register = template.Library()



@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError('Filter can only be applied to strings')
    banned_words = ['Some', 'badword2', 'badword3']
    for word in banned_words:
        if len(word) > 1:
            pattern = r'\b' + word + r'\b'
            value = re.sub(pattern, word[0] + '*' * (len(word) - 1), value, flags=re.IGNORECASE)
    return value