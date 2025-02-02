from rest_framework import viewsets
from django.utils.translation import gettext as _
from django.core.cache import cache
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get("blog_posts")
        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set("blog_posts", response.data, timeout=60)  # Cache for 1 minute
        return response
