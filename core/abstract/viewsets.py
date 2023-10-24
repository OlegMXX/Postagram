from rest_framework import viewsets
from rest_framework import filters


class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']  # can be used as ordering pars in request
    ordering = ['-updated']
