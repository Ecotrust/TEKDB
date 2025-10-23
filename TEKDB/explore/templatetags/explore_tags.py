from django import template

register = template.Library()


@register.filter(name="mult")
def mult(value, arg):
    """Multiplies the value by the arg"""
    return int(value) * int(arg)


# redefining 'mult' from line 6, should this be 'subtract'?
@register.filter(name="subtract")
def mult(value, arg): # noqa: F811 
    """Subtracts the arg from the value"""
    return int(value) - int(arg)


# register.filter('mult', mult)
