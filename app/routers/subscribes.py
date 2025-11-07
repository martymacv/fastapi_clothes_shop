from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db_depends import get_async_db

from app.models.subscribes import SubscribeModel
from app.schemas.subscribes import SubscribeSchema, SubscribeCreate

router = APIRouter(
    prefix="/subscribes",
    tags=["subscribes"]
)


@router.get("/", response_model=list[SubscribeSchema])
async def get_all_subscribes(
        db: AsyncSession = Depends(get_async_db)
):
    """
    Получает список активных подписчиков на новости
    """
    scalars = await db.scalars(
        select(SubscribeModel)
        .where(SubscribeModel.is_active == True)
    )
    subscribes = scalars.all()
    return subscribes
