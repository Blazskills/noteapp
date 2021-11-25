from django.urls import path
from . import views
import django.contrib.auth.views as auth_views



app_name = 'blog'
urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('dashboard', views.DashboardView.as_view(), name='dashboard'),
     path('blogpostview', views.BlogPostView.as_view(), name='blogpostview'),
    # functon based url view
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.deletepost, name='delete'),

    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutpage, name='logout')

    

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote')

]
