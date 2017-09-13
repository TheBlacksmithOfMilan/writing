from django.shortcuts import render, get_object_or_404

def handler400(request):
    return render(request, 'error/400.html', status=400)

def handler403(request):
    return render(request, 'error/404.html', status=403)

def handler404(request):
    return render(request, 'error/404.html', status=404)

def handler500(request):
    return render(request, 'error/500.html', status=500)
