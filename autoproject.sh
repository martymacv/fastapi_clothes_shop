py -3.12 -m venv .venv
source .venv/Scripts/activate
mkdir app
mkdir app/routers
mkdir app/schemas
mkdir app/models
echo "# Точка входа приложения" > app/main.py
echo "# Настройка зависимостей для работы с БД" > app/db_depends.py
echo "# Настройки базы данных" > app/database.py
echo > app/__init__.py
echo > app/routers/__init__.py
echo > app/models/__init__.py
pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install asyncpg
pip install alembic
pip install loguru
pip freeze > requirements.txt
alembic init app/migrations
uvicorn app.main:app --reload --port 8000