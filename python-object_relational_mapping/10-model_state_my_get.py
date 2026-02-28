#!/usr/bin/python3
"""Print the id of a State object with a given name from hbtn_0e_6_usa.

Connects to a local MySQL server and prints the id of the State object
whose name matches the argument. The query is SQL injection safe.
If no matching state exists, prints 'Not found'.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    """Retrieve and print the id of the State with the given name."""
    if len(sys.argv) != 5:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id)
        .first()
    )

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
