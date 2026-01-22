# wordcnt 패키지 안의 urls 모듈
# wordcnt/ : name=wordcnt:wordinput
# wordcnt/about/: name=wordcnt:abount
# wordcnt/result/: name=wordcnt:result
from django.urls import path
from wordcnt import views
app_name = "wordcnt"
urlpatterns = [
    path("", views.wordinput, name="wordinput"),
    path("about/", views.about, name="about"),
    path("result/", views.result, name="result"),
]