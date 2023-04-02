from django import template
from menu.models import Menu


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, title):
    root = Menu.objects.get(title=title)
    url = context['item'] if 'item' in context else context['menu'] if 'menu' in context else ''
    ctx = {
        'root': root,
        'active': ''
    }

    for child in root.get_descendants(include_self=True):
        if child.slug == url:
            ctx['active'] = child
            break

    return ctx

