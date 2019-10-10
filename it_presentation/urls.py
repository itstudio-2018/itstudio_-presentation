"""it_presentation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from show.views import index_html, index_html_mobile
from . import general

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^404/', general.page_success),
    url(r'^show/', include('show.urls', namespace='show')),
    url(r'^join/', include('join.urls', namespace='join')),
    url(r'^mobile', index_html_mobile),
    url(r'^$', index_html),

    url(r'^js/(.+)', general.js_redirect),
    url(r'^css/(.+)', general.css_redirect),
    url(r'^dist/(.+)', general.dist_redirect),
    url(r'^templates/(.+)', general.templates_redirect),

    url(r'^captcha/', general.captcha_img),
]   \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
	      + static(settings.STATIC_URL)
handler404 = general.page404
handler500 = general.page404
handler502 = general.page404
