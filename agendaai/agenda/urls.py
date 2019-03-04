from agenda import views
from django.urls import path, include
#from rest_framework.authtoken import views as token
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
	path('category/',views.CategoryList.as_view(), name=views.CategoryList.name),
	path('category/<int:pk>/', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
	path('business/',views.BusinessList.as_view(), name=views.BusinessList.name),
	path('business/<int:pk>/', views.BusinessDetail.as_view(), name=views.BusinessDetail.name),
	path('user-create/',views.UserCreate.as_view(), name=views.UserCreate.name),
	path('user/',views.UserList.as_view(), name=views.UserList.name),
	path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
	path('address/',views.AddressList.as_view(), name=views.AddressList.name),
	path('address/<int:pk>/', views.AddressDetail.as_view(), name=views.AddressDetail.name),
	path('profession/',views.ProfessionList.as_view(), name=views.ProfessionList.name),
	path('profession/<int:pk>/', views.ProfessionDetail.as_view(), name=views.ProfessionDetail.name),
	path('professional/',views.ProfessionalList.as_view(), name=views.ProfessionalList.name),
	path('professional/<int:pk>/', views.ProfessionalDetail.as_view(), name=views.ProfessionalDetail.name),
	path('day/',views.DayList.as_view(), name=views.DayList.name),
	path('day/<int:pk>/', views.DayDetail.as_view(), name=views.DayDetail.name),
	path('horario/',views.HorarioList.as_view(), name=views.HorarioList.name),
	path('horario/<int:pk>/', views.HorarioDetail.as_view(), name=views.HorarioDetail.name),
]