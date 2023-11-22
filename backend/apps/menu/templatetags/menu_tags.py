from django import template
from menu.models import MenuItem, Menu
from django.db.models import Count


register = template.Library()

@register.inclusion_tag('menu/menu_template.html')
def draw_menu(menu_id, data = False, parent = False, obj = False):
    if not parent:
        data = sorted(list(MenuItem.objects.filter(menu_name=menu_id).values()), key=lambda x: x['title'])
        for d in data:
            d['children']=0
            for i in data:
                if i['parent_id']==d['id']:
                    d['children']+=1
        return {'menu_items': [i for i in data if i['parent_id']==None], 'menu_id': menu_id, 'data': data, 'obj':obj}

    menu_items = [i for i in data if i['parent_id']==parent['id']]
    return {'menu_items': menu_items, 'menu_id': menu_id, 'data': data, 'obj':obj}


@register.simple_tag()
def get_menu_names():
    return Menu.objects.annotate(Count('menuitem'))