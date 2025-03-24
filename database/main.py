from .connect import engine
from sqlalchemy.orm import Session
from .models.table import TokenUser, UserFileStorage


session = Session(engine)


def insertToken(token: str):
    "Создание токена"

    if checkToken(token):
        return {"status_code": 404, "title": "Ошибка", "discribe": "Токен уже существует"}
    
    session.add(TokenUser(token=token))
    session.commit()


def checkToken(token: str):
    """Получаем токен"""
    token = session.query(TokenUser).filter(TokenUser.token == token).all()
    if len(token) > 0:
        return True
    else:
        return False


def deleteToken(id: int | None = None, token: str | None = None):
    """Удаляем токен"""
    if id is None and token is None:
        return {"status_code": 400, "title": "Ошибка", "discribe": "Не указан один из ключевых параметров"}
    elif id is None and token is not None:
        session.query(TokenUser).filter(TokenUser.token == token).delete()
    elif id is not None and token is None:
        session.query(TokenUser).filter(TokenUser.id == id).delete()
    else:
        session.query(TokenUser).filter(TokenUser.token == token, TokenUser.id == id).delete()
    session.commit()
    return {"status_code": 200, "title": "Успешно", "discribe": None}


def insertFile(user: int, name: str,
               size: str, path: str, disc: str):
    """Загрузка в папку"""
    session.add(UserFileStorage(user=user, name=name, size=size, path=path, disc=disc))
    session.commit()
    return {"status_code": 200, "title": "Успешно", "discribe": None}


def selectFiles(token: str) -> list:
    """Список"""

    result = session.query(UserFileStorage).join(TokenUser).filter(TokenUser.token == token).all()
    list_files = [(x.id, x.name, x.size, x.disc) for x in result]
    return list_files


def selectIdUser(token: str) -> int:
    token = session.query(TokenUser).filter(TokenUser.token == token).all()
    if len(token) > 0:
        return token[0].id
    else:
        return False


def selectPathFile(token: str, id: int) -> str:
    """
        token: token user
        id: id file
    """

    result = session.query(UserFileStorage.path).join(TokenUser).filter(TokenUser.token == token, UserFileStorage.id == id).scalar()
    if result is None:
        return {"status_code": 404, "title": "Ошибка", "discribe": "Файл не найден"}
    else:
        return {"status_code": 200, "title": "Успешно", "discribe": result}