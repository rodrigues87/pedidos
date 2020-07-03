from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import *
from produtos.views import *

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('login/', login_user),
        path('login/submit', submit_login),
        path('', administrador),
        path('logout/', logout),
        path('produtos/', include('produtos.urls')),
        path('base/', base),
        path('pedidos/', include('core.urls'))

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,
                                                                               document_root=settings.STATIC_ROOT)
