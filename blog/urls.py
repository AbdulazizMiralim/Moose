from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('blog/<int:pk>/', blog_singel_view),
    path('about/', about_view),
    path('contact/', contact_view),

]
