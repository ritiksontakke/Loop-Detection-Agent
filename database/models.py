from sqlalchemy import BigInteger, Text, DateTime, Identity, func
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=False),
        primary_key=True
    )

    customer_name: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    product: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    def __repr__(self):
        return (
            f"Order(id={self.id}, "
            f"customer={self.customer_name}, "
            f"product={self.product}, "
            f"status={self.status})"
        )