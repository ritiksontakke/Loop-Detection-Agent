from sqlalchemy import select

from database.connection import SessionLocal
from database.models import Order


def get_all_orders():

    with SessionLocal() as session:

        statement = select(Order)

        orders = session.scalars(statement).all()

        for order in orders:
            print(order)


if __name__ == "__main__":
    get_all_orders()