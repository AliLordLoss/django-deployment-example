from django import template


register = template.Library()


@register.filter(name='camel_case')
def camel_case(value):
    res = ''
    res += value[0].upper()
    for i in range(1, len(value)):
        if value[i - 1] == ' ' or value[i - 1] == '\n':
            res += value[i].upper()
            continue
        res += value[i]
    return res


# register.filter('camel_case', camel_case)
