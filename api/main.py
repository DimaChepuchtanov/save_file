from fastapi import FastAPI,  Request, Depends, HTTPException, File, Form, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from typing import Annotated
from database import main
from dotmap import DotMap
from .templates import main as tempplate
import os

app = FastAPI()


def get_token(token: str):
    if bool(main.checkToken(token)) is not True and token != "18092001":
        raise HTTPException(status_code=401, detail="Token invalid")
    return token


@app.get("/insertUser")
def get_insert_user(newToken: str, dependencies=Depends(get_token)):

    result = DotMap(main.insertToken(newToken))
    if result.status_code == 404:
        return HTMLResponse(f"<h1>{result.discribe}</h1>")

    return HTMLResponse("<h1>Успешно</h1>")


@app.get("/deleteUser")
def delete_delete_user(userToken: str, dependencies=Depends(get_token)):
    result = DotMap(main.deleteToken(token=userToken))
    if result.status_code == 200:
        return HTMLResponse("<h1>Успешно</h1>")
    else:
        return HTMLResponse(f"<h1>{result.discribe}</h1>")        


@app.get("/getFiles")
def get_filestorage_list(dependencies: str = Depends(get_token)):
    """Получаем список файлов от пользователя"""

    token = dependencies
    table = """<table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background-color: #f2f2f2; text-align: center;">
                            <th>id</th>
                            <th>name</th>
                            <th>size</th>
                            <th>disc</th>
                        </tr>
                    </thead>
                    <tbody>
            """
    for i in main.selectFiles(token=token):
        table += f"""<tr style="text-align: center;">
                        <td style="border: 1px solid #ddd; padding: 8px;">{i[0]}</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{i[1]}</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{i[2]}</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{i[3]}</td>
                     </tr>
                  """

    table += "</tbody></table>"

    return HTMLResponse(table)


@app.get("/uploadFile")
def get_upload_file(dependencies: str = Depends(get_token)):
    return HTMLResponse(tempplate.upload_file(dependencies))


@app.post('/upload')
def upload_file(file: UploadFile, dependencies: str = Depends(get_token)):

    with open(os.getcwd() + f"/storageFile/{dependencies}/{file.filename}", "wb") as f:
        f.write(file.file.read())

    result = DotMap(user=main.insertFile(user=main.selectIdUser(dependencies),
                    name=file.filename,
                    size=str(file.spool_max_size * 0.000125) + " КБ",
                    path=os.getcwd() + f"/storageFile/{dependencies}/{file.filename}",
                    disc="-"))

    if result.status_code == 200:
        return HTMLResponse("<h1>Успешно</h1>")
    else:
        return HTMLResponse(f"<h1>{result.discribe}</h1>")


@app.get("/download")
def download_file(id: int, token: str = Depends(get_token)):
    path = DotMap(main.selectPathFile(token, id))

    file_name = path.discribe.split("/")[-1]
    if path.status_code == 404:
        return HTMLResponse("<h1>Файл не найден</h1>")
    else:
        return FileResponse(path.discribe, filename=file_name)
