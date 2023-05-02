# URL Shortener
URL shortener application implemented in Django, with the ability to deploy via docker compose.

## Technology stack
- Backend: Django 4.2
- Frontend: Materialize CSS
- DB: Postgres
- WSGI: gunicorn
- Web server: nginx
- Containerization: Docker and Docker Compose

## Preliminary steps
Rename the `env-sample` directory to `env`. Set the necessary values for environment variables.

## Development deployment
Env files used: `.env.dev`, `.env.dev.db`.
Run command:
```
docker compose up -d --build
```

## Production deployment
Env files used: `.env.prod`, `.env.prod.db`.
Run command:
```
docker compose -f docker-compose.prod.yml up -d --build
```

## Production deployment for using reverse proxy
Env files used: `.env.prod`, `.env.prod.db`, `.env.prod.proxy`.
Run command:
```
docker compose -f docker-compose.prod.for-reverse-proxy.yml up -d --build
```

## Next steps
1. Apply migrations:
```
docker compose [-f <file_name.yml>] exec web python manage.py migrate
```
2. Collect static:
```
docker compose [-f <file_name.yml>] exec web python manage.py collectstatic
```
3. Create superuser:
```
docker compose [-f <file_name.yml>] exec web python manage.py createsuperuser
```

## Author
Alexander Aravin - [sander-raven](https://github.com/sander-raven). Email: sander-raven@yandex.ru.

## License
The project is under the MIT license. For details, see the [LICENSE](LICENSE) file.
