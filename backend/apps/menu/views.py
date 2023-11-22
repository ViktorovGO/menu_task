from django.shortcuts import render, redirect
from menu.models import MenuItem
from django.shortcuts import get_object_or_404





def menu_view(request):

    # data = list(MenuItem.objects.values())
    # for d in data:
    #     d['children']=0
    #     for i in data:
    #         if i['parent_id']==d['id']:
    #             d['children']+=1

    return render(request,'menu/index.html', )



def dynamic_view(request, params):
    obj = get_object_or_404(MenuItem, url=params)
    return render(request,'menu/index.html', context={'obj':obj})