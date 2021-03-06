from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers


class HelloApiView(APIView):
    """Test API View."""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, requet, format=None):
        """Returns a list of APIViews features."""
        
        an_apiviews = [
            'Uses HTTP methods as the functions (get, post, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over logic',
            'Is mapped manually to URLS',
        ]
    
        return Response({'message': 'Hello!', 'an_apiview': an_apiviews})
    
    def post(self, request):
        """Create a hello message with our name."""
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handles updating an object."""
        
        return Response({'method': 'put'})
    
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""
        
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """Deletes and objects."""
        
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

