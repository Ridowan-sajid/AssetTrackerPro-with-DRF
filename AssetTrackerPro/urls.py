from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Asset import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('company/register/', views.CompanyCreate.as_view()),
    path('user/', views.UserCreateList.as_view()),
    path('user/<int:pk>/', views.UserDeleteUpdateRetrieve.as_view()),
    path('gadget/', views.GadgetCreateList.as_view()),
    path('gadget/<int:pk>/', views.GadgetDeleteUpdateRetrieve.as_view()),
    path('company/login/', views.CompanyLogin.as_view()),
    path('company/logout/', views.CompanyLogout.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
