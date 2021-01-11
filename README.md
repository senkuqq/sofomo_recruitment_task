# Sofomo recruitment task

Application for fetching and storing geolocation data from ipstack.com.

Application is able to add, delete or provide geolocation data on the base of ip address or URL. 

# Building

```sh
$ git clone https://github.com/senkuqq/sofomo_recruitment_task.git
$ cd sofomo_recruitment_task
$ docker build -t web:latest .
```

# Running the application
Run docker image.
```sh
$ docker run -d --name app -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
```

To ensure everything is running properly run.

```sh
$ docker exec -it app python manage.py test
```
Create superuser.
```sh
$ docker exec -it app python manage.py createsuperuser
```
Endpoints api/v1/token/ and api/v1/token/refresh/ are for obtaining and refreshing tokens.

Endpoints api/v1/geolocations/ is for creating and listing geolocations.

# Online
You can check online version on [heroku](https://sofomo-recruitment.herokuapp.com/api/v1/).

There is file sofomo-recruitment-heroku.postman_collection.json which You can import to Postman and try endpoints by yourself! 

# Heroku credentials

Login: Admin

Password: Admin


# Comments
* sqlite3 (default database) doesn't support large decimals so lattidue and longitude will be rounded.
