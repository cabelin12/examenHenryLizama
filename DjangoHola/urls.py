from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns ('',

    #(r'^$', 'HolaMundo.views.dame_sabores'),
    (r'^$', 'HolaMundo.views.mostrarTabla'),
    url(r'registro/', 'HolaMundo.views.formulario'),
    #url(r'^Holamundo/','DjangoHola.HolaMundo.views.dame_sabores'),
    # Examples:
    # url(r'^$', 'DjangoHola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
)

