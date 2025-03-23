from django.urls import include, path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from users.apis import user_collection, user_data
from users.views import (
    logout_view,
    user_registration
)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', user_registration, name='register'),
    path('logout/', logout_view, name='logout'),
    # path('', include(([
    #     path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    #     path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    # ], 'auth_api'))),
    #  path('api/users/', include(([
    #     path('', user_collection, name='collection'),
    #     path('<uuid:id>/', user_detail, name='data'),
    # ], 'users_api'))),
]