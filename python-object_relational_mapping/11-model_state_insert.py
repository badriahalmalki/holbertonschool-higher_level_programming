#!/usr/bin/python3
"""Add the State object 'Louisiana' to the hbtn_0e_6_usa database.

Connects to a local MySQL server and inserts a new State object with the
name 'Louisiana'. After creation, prints the new state's id.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    """Create a new State object and print its id."""
    if len(sys.argv) != 4:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
