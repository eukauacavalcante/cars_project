from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from cars.forms import CarModelForm
from cars.models import Car


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().select_related('brand').order_by('brand__name')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(
                Q(model__icontains=search) |
                Q(brand__name__icontains=search) |
                Q(plate__icontains=search) |
                Q(color__icontains=search)
            ).distinct()
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class NewCarCreateView(CreateView, LoginRequiredMixin):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/'


class CarUpdateView(UpdateView, LoginRequiredMixin):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView, LoginRequiredMixin):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/'
