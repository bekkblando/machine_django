from django.shortcuts import render, render_to_response
from django.template import RequestContext
from learndjango.models import Graph
import pickle
# Create your views here.
from django.views.generic import DetailView, ListView


class GraphView(ListView):
    model = Graph


def predict(request):
    context = {}
    print("hello")
    if request.POST:
        print("YO")
        number = int(str(request.POST.getlist('predict')[0]))
        predict = Graph.objects.all()[0]
        equation = pickle.loads(predict.fitequation)
        prediction = equation.predict(number)
        prediction = prediction[0][0]
        print(prediction)
        context['prediction'] = prediction
    return render_to_response(template_name="predict.html", context=context, context_instance = RequestContext(request))