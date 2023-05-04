from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from item.models import Item, Category

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query))

    return render(request, 'dashboard/index.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })
