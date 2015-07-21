from django.shortcuts import render
from learndjango.models import Graph
# Create your views here.
from django.views.generic import DetailView, ListView


class GraphView(ListView):
    model = Graph
