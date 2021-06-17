from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from alumnos.forms import AlumnoForm
from alumnos.models import Alumno


class AlumnosListView(ListView):
    model = Alumno
    template_name = 'alumnos/lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Alumnos'
        context['formpage'] = reverse_lazy('alumnos:alumnos_new')
        return context


class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnos/form.html'
    success_url = reverse_lazy('alumnos:alumnos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Alumnos'
        context['listpage'] = self.success_url
        context['action_form'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action_form']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Action invalid'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnos/form.html'
    success_url = reverse_lazy('alumnos:alumnos_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Alumnos'
        context['listpage'] = self.success_url
        context['action_form'] = 'edit'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action_form']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Action invalid'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


class AlumnoDelete(View):
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            cate = Alumno.objects.get(pk=request.POST['id'])
            cate.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
