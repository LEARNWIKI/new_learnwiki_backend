from django.shortcuts import render
from django.contrib.auth import login
from django.utils import timezone
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    GenericAPIView
)
from .models import (
    Node,
    Link
)
from .serializers import (
    NodeSerializer,
    LinkSerializer
)


class NodeListView(ListAPIView):
    queryset = Node
    serializer_class = NodeSerializer

    def get(self, request):
        try:
            node = self.queryset.objects.all()
        except Node.DoesNotExist:
            return Response(
                data={"description": "Ячейки не найдены", 
                      "error": "node_not_found"}, 
                status=404)

        serializer = self.serializer_class(node, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class LinkListView(ListAPIView):
    queryset = Link
    serializer_class = LinkSerializer

    def get(self, request):
        try:
            node = self.queryset.objects.all()
        except Link.DoesNotExist:
            return Response(
                data={"description": "Ячейки не найдены", 
                      "error": "node_not_found"}, 
                status=404)

        serializer = self.serializer_class(node, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
