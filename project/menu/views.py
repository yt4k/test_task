from django.shortcuts import render


def home_category_view(request, path=None):
    current_path = f"/{path}/" if path else '/'

    context = {
        'current_path': current_path
    }
    return render(request, 'menu/home.html', context)