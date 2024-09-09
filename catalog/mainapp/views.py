from django.db.models import Count
from mainapp.models import Product, Param
from mainapp.serializers import ProductSerializer, ParamCountSerializer, ParamSerializer
from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        param_name = self.request.query_params.get('param_name')
        param_val = self.request.query_params.get('param_val')
        if param_name:
            queryset = queryset.filter(param__name=param_name.title()).distinct()
        if param_val:
            try:
                param_val = float(param_val)
                queryset = queryset.filter(param__value=param_val).distinct()
            except ValueError:
                pass
        return queryset


class ParamViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ParamSerializer

    def filter_queryset(self, queryset):
        params_ids = Product.objects.values_list('param', flat=True).distinct()
        return Param.objects.filter(id__in=params_ids)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ParamCountViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.values('param').annotate(param_count=Count('param'))
    serializer_class = ParamCountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
