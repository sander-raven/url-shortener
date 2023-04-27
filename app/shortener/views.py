from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from shortener.forms import ShortURLForm
from shortener.models import ShortURL


def index_view(request):
    template = 'shortener/index.html'
    context = {
        'form': ShortURLForm,
    }

    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                owner = request.user
            else:
                owner = None
            if form.cleaned_data['short_code']:
                short_url, _ = ShortURL.objects.get_or_create(
                    original_url=form.cleaned_data['original_url'],
                    short_code=form.cleaned_data['short_code'],
                    owner=owner,
                )
            else:
                # short_url, _ = ShortURL.objects.get_or_create(
                #     original_url=form.cleaned_data['original_url'],
                #     owner=owner,
                # )
                short_url = ShortURL.objects.filter(
                    original_url=form.cleaned_data['original_url'],
                    owner=owner,
                ).first()
                if not short_url:
                    short_url = ShortURL.objects.create(
                        original_url=form.cleaned_data['original_url'],
                        owner=owner,
                    )
            context['original_url'] = short_url.original_url
            context['new_url'] = (
                request.build_absolute_uri('/') + short_url.short_code
            )
        else:
            context['errors'] = form.errors

    return render(request, template, context)


def redirect_view(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code__iexact=short_code)
    short_url.increase_number_of_transitions()
    return HttpResponseRedirect(short_url.original_url)
