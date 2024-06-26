from django.shortcuts import render
from . import models, forms
from django.views import generic


class SportListView(generic.ListView):
    template_name = 'sport/sport_app.html'
    context_object_name = 'sport_app_list'
    model = models.Quote
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.YTVideo.objects.order_by('-id')
        context['top_product'] = models.Topfive.objects.order_by('-id')
        return context



