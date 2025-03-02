from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from Users.views import login,logoutUser, register, recoverAccount, redefinePassword, pagConfig, editar_usuario, configPassword, update_photo, delete_photo
from guest.views import index, competition, admission
from members.views import *
from report.views import *
from django.conf import settings
from django.conf.urls.static import static
from stock.views import stock
from report.views import meetings, flights



urlpatterns = [

    path('admin/', admin.site.urls),

    # Users
    path('login/', login, name='login'),
    path('logoutUser/', logoutUser, name='logoutUser'),
    path('register/', register, name='register'),
    path('configPassword/', configPassword, name='configPassword'),
    path('account_recovery/', recoverAccount, name='recoverAccount'),
    path('redefine_password/<str:username>/<str:token>', redefinePassword, name="redefinePassword"),
    path ('pagConfig/', pagConfig, name = 'pagConfig'),
    path('editar/', editar_usuario, name='editar_usuario'),
    path("pagConfig/update_photo/", update_photo, name="update_photo"),
    path("pagConfig/delete_photo/", delete_photo, name="delete_photo"),

    # guest
    path('', index, name="index"),
    path('competition/', competition, name="competition"),
    path('admission/', admission, name="admission"),

    # report
    path('report/', include('report.urls')),
    path('meetings/', meetings, name='meetings'),
    path('flights/', flights, name='flights'),
    path('', include('report.urls')),

    # members
    path('sidebar/', sidebar , name="sidebar"),
    path('create_task/', create_task, name= "create_task"),
    path('edit_task/', edit_task, name= "edit_task"),
    path('delete_task/', delete_task, name= "delete_task"),
    path('Top/', Top, name='top'),
    path('members/', kanban_view, name='members'),
    path('members/', include('members.urls')),
    path('foto/', upload_photo, name='upload_photo'),
    path('home/', home, name="home"),
    path('create_post_or_event/', create_post_or_event, name='create_post_or_event'),
    path('get-events-tasks/', get_events_tasks, name='get_events_tasks'),
    path('previous-month/', previous_month, name='previous_month'),
    path('next-month/', next_month, name='next_month'),

    # stock
    
    path('stock/', stock, name='stock'),
    path('', include('stock.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

