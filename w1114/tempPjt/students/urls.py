from django.urls import path,include
from . import views    # . 현재라는 뜻 / view에서 모든 페이지를 분배시킴(model에 연결해줌)

app_name = 'students' 
urlpatterns = [
    ### path(url주소 , views함수명, url이름)
    # http://127.0.0.1:8000/students/reg/ : url로 연결하는 방법(외부에서 접속되는 것은 무조건 이 방식)
    # students:reg : 이름으로 연결하는 방법(프로그램 내에서만 가능)
    path('reg/',views.regStudent,name='reg'),
]
