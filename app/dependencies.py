from fastapi import Header

from app.database import DBSession, sessionmanager


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


async def get_async_db():
    async with sessionmanager.session() as session:
        yield session


def get_list_headers(page_number: int = Header(default=0, alias="page"),
                     page_length: int = Header(default=100, alias="pagesize")):
    """
    Get the pagination headers from the request
    :param page_number: Page number to retrieve from the database (default: 0)
    :param page_length: Number of items per page (default: 100)
    :return: Dictionary with the pagination headers
    """
    return {
        "page": page_number,
        "pagesize": page_length
    }
