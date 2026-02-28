#!/usr/bin/python3
"""List all State objects from the hbtn_0e_6_usa database.

Connects to a local MySQL server and prints all State objects stored in the
database in the format "<id>: <name>", ordered by states.id in ascending
order.

Usage:
    ./7-model_state_fetch_all.py <mysql_user> <mysql_password> <database_name>
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def fetch_all_states(user, password, db_name):
    """Return a list of State objects ordered by id."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    session.close()
    return states


def main():
    """Parse CLI args and print each State as 'id: name'."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    for state in fetch_all_states(user, password, db_name):
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
