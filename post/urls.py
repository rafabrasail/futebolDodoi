from django.urls import path
from .views import (post_list_and_create, 
                    load_post_data_view, 
                    like_unlike_post, 
                    post_detail,
                    post_detail_data_view,
                    delete_post,
                    update_post,
                    image_upload_view)

app_name = 'post'

urlpatterns = [
    path('', post_list_and_create, name='main-board'),
    path('<pk>/', post_detail, name='post-detail'),
    # url same action on the html form
    path('upload/', image_upload_view, name='image-upload'),
    path('data/<int:num_posts>/', load_post_data_view, name='posts-data'),
    path('like-unlike/', like_unlike_post, name='posts-data'),
    path('<pk>/data/', post_detail_data_view, name='post-detail-data'),
    path('<pk>/update/', update_post, name='post-update'),
    path('<pk>/delete/', delete_post, name='post-delete'),
    
]
