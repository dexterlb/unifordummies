from django.shortcuts import render
from django.views.generic import ListView

from default import models


class ProgrammeListView(ListView):
    model = models.Programme
    templates = 'default/programme_list'
    context_object_name = 'programmes'


def index_page_view(request):
    spec_cat_cat = \
        models.SpecCategoryCategory.categories.all()
    return render('index.html', {spec_cat_cat: spec_cat_cat})
