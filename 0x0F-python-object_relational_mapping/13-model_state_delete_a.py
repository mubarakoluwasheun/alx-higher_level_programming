#!/usr/bin/python3
"""
Delete from table states with names containing letter 'a'.
Arguments: username, password, database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                            fromat(user, passwd, db), pool_pre_ping=True)
    Base./metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session =- Session()

    # find all appropriate states to be deleted
    states = session.query(State). filter(State.name.like('%a%')).all()
    for s in states:
        session.delete(s)

    session.commit()
    session.close()
    