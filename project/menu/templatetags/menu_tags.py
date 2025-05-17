from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    active_item = None
    for item in menu_items:
        if item.url == current_url:
            active_item = item
            break

    def build_tree(items, parent=None):
        result = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                is_active = (item == active_item) or any(
                    child['is_active'] for child in children
                )
                result.append({
                    'item': item,
                    'children': children,
                    'is_active': is_active
                })
        return result

    menu_tree = build_tree(menu_items)

    return {
        'menu_tree': menu_tree,
        'current_url': current_url
    }