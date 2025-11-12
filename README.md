# fastapi_clothes_shop

## Инструкция по Alembic миграции
```
alembic init -t async app/migrations
```
```
alembic revision --autogenerate -m "Initial migration for PostgreSQL"
```
```
alembic upgrade head
```
```
docker compose exec clothes_shop_api alembic upgrade head
```
