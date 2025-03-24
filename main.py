"""
    Главный файл, запуск.
"""

from api.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=5000)
