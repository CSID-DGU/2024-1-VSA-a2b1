from django.urls import path, include

urlpatterns = [
    path('', include('dj_rest_auth.urls')),  # 로그인/로그아웃, JWT 토큰 관리
    path('registration/', include('dj_rest_auth.registration.urls')),  # 회원가입
]
