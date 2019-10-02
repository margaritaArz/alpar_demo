from django.shortcuts import render


def main(request):
    context = {'test': 'test'}
    return render(request, 'mainapp/index.html', context)
