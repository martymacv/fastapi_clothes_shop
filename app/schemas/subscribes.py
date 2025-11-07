from pydantic import BaseModel, Field, ConfigDict, EmailStr


class SubscribeCreate(BaseModel):
    """
    Модель для создания новой подписки на новости
    """
    email: EmailStr = Field(
        description="Email подписчика"
    )
    is_active: bool = Field(
        description="Мягкое удаление подписчика"
    )


class SubscribeSchema(BaseModel):
    """
    Модель для учёта всех подписчиков новостей магазина
    """
    id: int = Field(
        description="Уникальный идентификатор подписчика"
    )
    email: EmailStr = Field(
        description="Email подписчика"
    )
    is_active: bool = Field(
        description="Мягкое удаление подписчика"
    )

    model_config = ConfigDict(from_attributes=True)
