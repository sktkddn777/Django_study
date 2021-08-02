## Django_study
 
1. 기본적인 장고 세팅과 간단한 앱을 구현해봅니다.
2. 도커를 활용하여 장고 개발환경을 구축합니다.
3. 장고 개발환경에 NGINX와를 추가합니다(아직)
4. 장고 프로젝트를 AWS에 배포합니다(아직)  
  
<br/>

## DB
- Database는 postgreSQL을 사용   
데이터베이스 migrate하는 방법.
> 1. models.py 에서 모델을 변경합니다.
> 2. python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
> 3. python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요.


## REST API
 1.CREATE: INSERT to create a new database record  
 2.READ: SELECT to retrieve data from a database table  
 3.UPDATE: UPDATES a record based on the specified primary key  
 4.DELETE: DELETES a row in a database table

##  참고 자료
(1) 장고 tutorial
https://docs.djangoproject.com/ko/3.2/intro/tutorial01/

(2) 장고 tutorial
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/skeleton_website



