#!/usr/bin/python3
"""Delete all State objects containing the letter 'a' from hbtn_0e_6_usa.

Connects to a local MySQL server and deletes all State objects whose
name contains the letter 'a'. Changes are committed to the database.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    """Delete all State objects with 'a' in their name."""
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

    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
