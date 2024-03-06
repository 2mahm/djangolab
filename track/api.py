from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import productd
from .serializer import ProductSerializer
@api_view(['GET'])
def product_list_api(request):
    products = productd.objects.all()
    data = ProductSerializer(products, many=True,context={'request':request}).data
    return Response({'products':data})
@api_view(['GET'])
def product_detail_api(request, product_id):
    product = productd.objects.get(id=product_id)
    data = ProductSerializer(product,context={'request':request}).data
    return Response({'product':data})
class ProductCraeteAPI(generics.CreateAPIView):
    queryset = productd.objects.all()
    serializer_class = ProductSerializer
class ProductUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = productd.objects.all()
    serializer_class = ProductSerializer
class ProductDeleteAPI(generics.DestroyAPIView):
    queryset = productd.objects.all()
    serializer_class = ProductSerializer