"""this file defines URL patterns for djangoapp"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'portfolioapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route = '', view = views.index, name='index'),
    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    # path for get dealership view

    # path for dealer reviews view

    # path for add a review view

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
