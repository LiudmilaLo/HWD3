from django import template


register = template.Library()


C_WORDS = {
    'блаблабла': 'б*',
    'Блаблабла': 'Б*',
    'глупая': 'г*',
    'глупый': 'г*',
}


@register.filter()
def censor(text):
    for word, initial in C_WORDS.items():
        text = text.replace(word.lower(), initial)
    return f'{text}'
