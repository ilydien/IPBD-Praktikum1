from sqlmodel import create_engine, Session

DATABASE_URL = "postgresql://admin:1234@localhost:5436/database-blog"

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
