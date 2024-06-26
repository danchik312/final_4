from django.shortcuts import render , get_object_or_404
from . import models, forms
from django.views import generic


class SportListView(generic.ListView):
    template_name = 'sport/sport_app.html'
    context_object_name = 'quote'
    model = models.Quote
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.YTVideo.objects.order_by('-id')
        context['top_product'] = models.Topfive.objects.order_by('-id')
        return context

class SportProductView(generic.ListView):
    template_name = "sport/sport_list.html"
    context_object_name = "sport"
    model = models.Sport_list
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sport"] = models.Sport_list.objects.order_by("-id")
        return context


class SportDetailView(generic.DetailView):
    template_name = "sport/sport_detal.html"
    context_object_name = "sport_id"

    def get_object(self, **kwargs):
        sport_id = self.kwargs.get("id")
        return get_object_or_404(models.Sport_list, id=sport_id)

def sport_tags_view(request):
    if request.method == "GET":
        youth_tags = models.Products.objects.filter(tags__name="youth").order_by("-id")
        return render(
            request,
            template_name="products/sport_tag.html",
            context={"youth_tags": youth_tags},
        )
def pensioner_tags_view(request):
    if request.method == "GET":
        pensioner_tags = models.Products.objects.filter(tags__name="pensioners").order_by("-id")
        return render(
            request,
            template_name="products/pensioner_tag.html",
            context={"pensioner_tags": pensioner_tags},
        )

def all_products(request):
    if request.method == "GET":
        products = models.Products.objects.filter().order_by("-id")
        return render(
            request,
            template_name="products/all_products.html",
            context={"products": products},
        )


