from django.urls import path
from django.conf import settings 

from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.apitest,name="apitest" ),
    path('match_info/<str:id>/<str:src>',views.match_info,name="match_info" ),
    path('live_scores/<str:id>',views.live_score,name="live_score"),
    path('alldetail/<str:id>',views.alldetail,name="alldetail"),

    path('scorelive/',views.scorelive,name="scorelive"),
    path('calender/',views.calender,name="calender"),

    path('matchinfo/',views.matchinfo,name="matchinfo"),
    path('ranking/',views.ranking,name="ranking"),
    path('admin/',views.admin,name="admin"),

    #path('calender/',views.calender,name="calender"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 