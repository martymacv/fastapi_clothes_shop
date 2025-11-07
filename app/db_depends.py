# Настройка зависимостей для работы с БД


from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker


# --------------- Асинхронная сессия -------------------------


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Предоставляет асинхронную сессию SQLAlchemy
    для работы с базой данных PostgreSQL.
    """
    async with async_session_maker() as session:
        yield session
