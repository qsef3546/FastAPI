from sqlmodel import Field, SQLModel, create_engine, Session, select
from sqlconf import config


engine = create_engine(str(config.SQLALCHEMY_DATABASE_URI))

class myuser(SQLModel, table=True):
    name: str | None = Field(default=None, primary_key=True)
    age: int | None = None

def selects():
    with Session(engine) as session:
        statement = select(myuser)
        res = session.exec(statement).all()
        s = {'res':[x.__dict__ for x in res]}
        return s
        
def insert(u:myuser):
    with Session(engine) as session:
        session.add(u)
        session.commit()

def update(u:myuser):
    with Session(engine) as session:
        statement = select(myuser).where(myuser.name == u.name)
        res = session.exec(statement).one()
        if res.name != u.name:
            res.name = u.name
        if (res.age != u.age) and u.age != None:
            res.age = u.age
        session.add(res)
        session.commit()

def delete(name:str):
    with Session(engine) as session:
        statement = select(myuser).where(myuser.name == name)
        res = session.exec(statement).one()
        session.delete(res)
        session.commit()
