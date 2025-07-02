from sqlalchemy.orm import mapped_column, Mapped


class IntPkMixin:
    """Базовый класс для интового id"""

    id: Mapped[int] = mapped_column(primary_key=True)
