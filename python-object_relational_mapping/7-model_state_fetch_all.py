#!/usr/bin/python3
"""
A script that lists all State objects
from the database hbtn_0e_6_usa using SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import session

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = session(engine)
    session = session()
    states = session.query(State).order_by(State.id.asc()).all

    for state in states:
        print("{}: {}".format(states.id, state.name))

    states = session.query(State).order_by(State.id.asc()).all

    session.close()
