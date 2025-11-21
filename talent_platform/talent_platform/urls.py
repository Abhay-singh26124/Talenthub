from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Our new app URLs
    path('jobs/', include('jobs.urls')),
    path('profile/', include('profiles.urls')),
    path('', include('applications.urls')), # For dashboard and apply
    
    # Authentication
    path('signup/', user_views.signup_choice, name='signup_choice'),
    path('signup/candidate/', user_views.candidate_signup, name='candidate_signup'),
    path('signup/recruiter/', user_views.recruiter_signup, name='recruiter_signup'),
    
    # Built-in Login/Logout
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)