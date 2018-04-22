from django import template

register = template.Library()

@register.filter(name='arrayEltByIndex')
def arrayEltByIndex(array,index):
	return array[index -1]
