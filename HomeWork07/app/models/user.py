from sqlalchemy.orm import mapped_column, Mapped, relationship

from .mixins.int_pk_mixin import IntPkMixin
from .base import Base


class User(IntPkMixin, Base):
    """
    Класс User
    От класса IntPkMixin приходит id
    От класса Base приходит tablename
    """

    name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(
        unique=True,
        default="",
        server_default="",
    )
    phone: Mapped[str] = mapped_column(
        unique=True,
        default="",
        server_default="",
    )
    website: Mapped[str] = mapped_column(
        unique=True,
        default="",
        server_default="",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" name={self.name!r},"
            f" phone={self.phone!r},"
            f" username={self.username!r},"
            f" email={self.email!r},"
            f" website={self.website!r},"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        return self.id == other.id
