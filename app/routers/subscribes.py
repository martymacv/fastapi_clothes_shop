from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, ScalarResult

from app.db_depends import get_async_db

from app.models.subscribes import SubscribeModel
from app.schemas.subscribes import SubscribeSchema, SubscribeCreate

router = APIRouter(
    prefix="/subscribes",
    tags=["subscribes"]
)


async def check_subscribe(
        subscribe_email: str,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Возвращает подписку, если она есть или None
    """
    scalar: ScalarResult[SubscribeModel | None] = await db.scalars(
        select(SubscribeModel)
        .where(
            SubscribeModel.email == subscribe_email
        )
    )
    subscribe = scalar.first()
    return subscribe


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


@router.post("/", response_model=SubscribeSchema)
async def activate_new_subscribe(
        new_subscribe: SubscribeCreate,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Создаёт новую подписку или активирует старую
    """
    subscribe = await check_subscribe(new_subscribe.email, db)
    if subscribe is None:
        subscribe = SubscribeModel(
            **new_subscribe.model_dump()
        )
        db.add(subscribe)
        await db.commit()
        await db.refresh(subscribe)
    elif subscribe.is_active:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You already have an active subscription!"
        )
    else:
        subscribe.is_active = True
        await db.commit()
    return subscribe


@router.delete("/")
async def deactivate_subscribe(
        email: str,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Деактивирует подписку
    """
    subscribe = await check_subscribe(email, db)
    if subscribe is None or not subscribe.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subscribe not found"
        )
    subscribe.is_active = False
    await db.commit()
    return {
        "message": "Your subscribe has been deactivated!"
    }
