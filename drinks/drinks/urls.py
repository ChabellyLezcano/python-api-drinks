from django.contrib import admin
from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

# Define your URL patterns as before
urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail),
]

# Wrap the urlpatterns with format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)