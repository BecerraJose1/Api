import secrets
import uvicorn
import asyncio
import json
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import mysql.connector
import config
from datetime import datetime
import pytz
app = FastAPI()

from db_model import (
    File1,
    File2,
    File_ciudad,
    File3,
    Filec,
    LoginRequest,
    User,
    LoginResponse,
    FilecCreate,
    File1Create,
    File3Create
)

# API Instance
app = FastAPI()
app.title = "API MAXIMO"
app.version = "0.0.1"

# Database configuration
connection = mysql.connector.connect(**config.db)
cursor = connection.cursor()

def user_to_dict(user):
    """
    Convert a user object to a dictionary.

    Args:
        user: User object to be converted.

    Returns:
        A dictionary representation of the user.
    """
    return {
        "id": user.id,
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email,
    }



@app.get('/')
def main():
    """
    Root endpoint of the API.

    Returns:
        A simple JSON response indicating the API name.
    """
    return {"Api MAXIMO"}
    

@app.post('/login')
def login(login_request: LoginRequest):
    """
    Endpoint for user login.

    Args:
        login_request: Request data containing email and password for login.

    Returns:
        LoginResponse with a token if login is successful.
    """
    # Implementation of the login logic goes here
    cursor.execute("SELECT email, password FROM users WHERE email = %s", (login_request.email,))
    user_data = cursor.fetchone()

    if user_data is None or user_data[1] != login_request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = secrets.token_urlsafe(32)
    cursor.execute("UPDATE users SET token = %s WHERE email = %s", (token, login_request.email))
    connection.commit()

    return LoginResponse(token=token)

@app.get("/get_file3/", response_model=List[File3])
def get_file3(request: Request):

        # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    

    # The token is valid, get the list of comprobantes
    cursor.execute("SELECT * FROM file3")
    file3_data = cursor.fetchall()

    file3 = [File3(idfile3=idfile3, cedula=cedula, nombre1=nombre1, nombre2=nombre2, apellido1=apellido1, apellido2=apellido2, direccion=direccion, celular=celular, correo=correo, id_ciudad=id_ciudad) for idfile3, cedula, nombre1, nombre2, apellido1, apellido2, direccion, celular, correo, id_ciudad in file3_data ]
    return file3


@app.get("/get_file_ciudad/", response_model=List[File_ciudad])
def get_file_ciudad(request: Request):

        # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    

    # The token is valid, get the list of comprobantes
    cursor.execute("SELECT * FROM file_ciudad")
    file_ciudad_data = cursor.fetchall()

    file_ciudad = [File_ciudad(idfile_ciudad=idfile_ciudad, nombre_ciudad=nombre_ciudad) for idfile_ciudad, nombre_ciudad in file_ciudad_data ]
    return file_ciudad


@app.get("/get_file_c/", response_model=List[Filec])
def get_filec(request: Request):

        # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    

    # The token is valid, get the list of comprobantes
    cursor.execute("SELECT * FROM filec")
    comprobantes_data = cursor.fetchall()

    filec = [Filec(idfilec=idfilec, comprobante=comprobante, nombre=nombre, tipo=tipo) for idfilec, comprobante, nombre, tipo in comprobantes_data ]
    return filec

@app.post("/create_file3/", response_model=File3)
def create_file3(request:Request, file3_data:File3Create):
    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    #El token es válido crea un registro en File1
    try:
        cursor.execute("INSERT INTO file3 (cedula, nombre1, nombre2,apellido1, apellido2, direccion, celular, correo, id_ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (file3_data.cedula, file3_data.nombre1, file3_data.nombre2, file3_data.apellido1, file3_data.apellido2, file3_data.direccion, file3_data. celular, file3_data.correo, file3_data.id_ciudad))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error during insertion: {err}")
    # Obtén el ID del registro recién creado
    cursor.execute("SELECT LAST_INSERT_ID()")
    new_id = cursor.fetchone()[0]

    # Obtiene los datos del registro recién creado
    cursor.execute("SELECT * FROM file3 WHERE idfile3 = %s", (new_id,))
    file3_record = cursor.fetchone()

    if file3_record is None:
        raise HTTPException(status_code=500, detail="Failed to create the file3 record")

    # Crea un objeto File3 y lo devuelve como respuesta
    idfile3, cedula, nombre1, nombre2, apellido1, apellido2, direccion, celular, correo, id_ciudad = file3_record
    file3 = File3(idfile3=idfile3, cedula=cedula, nombre1=nombre1, nombre2=nombre2, apellido1=apellido1, apellido2=apellido2, direccion=direccion, celular=celular, correo=correo, id_ciudad=id_ciudad)
    return file3


@app.put("/edit_file3/{idfile3}", response_model=File3)
def edit_file3(request: Request, idfile3: int, file3_data: File3Create):
    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Verifica si el registro con el idfile3 especificado existe
    cursor.execute("SELECT * FROM file3 WHERE idfile3 = %s", (idfile3,))
    existing_record = cursor.fetchone()
    
    if existing_record is None:
        raise HTTPException(status_code=404, detail="File3 record not found")

    # El token es válido, actualiza el registro en File3
    try:
        cursor.execute("UPDATE file3 SET cedula = %s, nombre1 = %s, nombre2 = %s, apellido1 = %s, apellido2 = %s, direccion = %s, celular = %s, correo = %s, id_ciudad = %s WHERE idfile3 = %s",
                       (file3_data.cedula, file3_data.nombre1, file3_data.nombre2, file3_data.apellido1, file3_data.apellido2, file3_data.direccion, file3_data.celular, file3_data.correo, file3_data.id_ciudad, idfile3))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error during update: {err}")

    # Obtén los datos del registro actualizado
    cursor.execute("SELECT * FROM file3 WHERE idfile3 = %s", (idfile3,))
    updated_record = cursor.fetchone()

    if updated_record is None:
        raise HTTPException(status_code=500, detail="Failed to update the file3 record")

    # Crea un objeto File3 y lo devuelve como respuesta
    idfile3, cedula, nombre1, nombre2, apellido1, apellido2, direccion, celular, correo, id_ciudad = updated_record
    file3 = File3(idfile3=idfile3, cedula=cedula, nombre1=nombre1, nombre2=nombre2, apellido1=apellido1, apellido2=apellido2, direccion=direccion, celular=celular, correo=correo, id_ciudad=id_ciudad)
    return file3


@app.post("/create_file1/", response_model=File1)
def create_file1(request: Request, file1_data:File1Create):
    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    #El token es válido crea un registro en File1
    try:
        cursor.execute("INSERT INTO file1 (id_comprobante, fecha_documento, documento,id_cuenta, id_cedula, id_c_costos, factura, valor, tipo, concepto, fecha_insert, fecha_update) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (file1_data.id_comprobante ,file1_data.fecha_documento, file1_data.documento,file1_data.id_cuenta,file1_data.id_cedula,file1_data.id_c_costos ,file1_data.factura, file1_data.valor, file1_data.tipo, file1_data.concepto, file1_data.fecha_insert, file1_data.fecha_update))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error during insertion: {err}")
    # Obtén el ID del registro recién creado
    cursor.execute("SELECT LAST_INSERT_ID()")
    new_id = cursor.fetchone()[0]

    # Obtiene los datos del registro recién creado
    cursor.execute("SELECT * FROM file1 WHERE idFile1 = %s", (new_id,))
    filec_record = cursor.fetchone()

    if filec_record is None:
        raise HTTPException(status_code=500, detail="Failed to create the filec record")

    # Crea un objeto Filec y lo devuelve como respuesta
    idFile1, id_comprobante, fecha_documento, documento, id_cuenta, id_cedula, id_c_costos, factura, valor, tipo, concepto, fecha_insert, fecha_update = filec_record
    file1 = File1(idFile1=idFile1, id_comprobante=id_comprobante, fecha_documento=fecha_documento, documento=documento, id_cuenta=id_cuenta, id_cedula=id_cedula, id_c_costos=id_c_costos, factura=factura, valor=valor, tipo=tipo, concepto=concepto, fecha_insert=fecha_insert, fecha_update=fecha_update)
    return file1

@app.delete("/delete_file1/{id}")
def delete_file1(id: int, request: Request):
    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Verifica si el registro a eliminar existe
    cursor.execute("SELECT * FROM file1 WHERE idFile1 = %s", (id,))
    file1_record = cursor.fetchone()

    if file1_record is None:
        raise HTTPException(status_code=404, detail="File1 record not found")

    # Si el registro existe, procede a eliminarlo
    cursor.execute("DELETE FROM file1 WHERE idFile1 = %s", (id,))
    connection.commit()

    return {"message": f"File1 record with ID {id} has been deleted"}

@app.delete("/delete_file3/{id}")
def delete_file3(id: int, request: Request):
    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Verifica si el registro a eliminar existe
    cursor.execute("SELECT * FROM file3 WHERE idfile3 = %s", (id,))
    file3_record = cursor.fetchone()

    if file3_record is None:
        raise HTTPException(status_code=404, detail="File3 record not found")

    # Si el registro existe, procede a eliminarlo
    cursor.execute("DELETE FROM file3 WHERE idfile3 = %s", (id,))
    connection.commit()

    return {"message": f"File3 record with ID {id} has been deleted"}

@app.post("/create_file_c/", response_model=Filec)
def create_filec(request: Request, filec_data: FilecCreate):

    # Verifica el token proporcionado
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # El token es válido, crea un nuevo registro en la tabla filec
    try:
        cursor.execute("INSERT INTO filec (comprobante, nombre, tipo) VALUES (%s, %s, %s)", (filec_data.comprobante, filec_data.nombre, filec_data.tipo))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error during insertion: {err}")

    # Obtén el ID del registro recién creado
    cursor.execute("SELECT LAST_INSERT_ID()")
    new_id = cursor.fetchone()[0]

    # Obtiene los datos del registro recién creado
    cursor.execute("SELECT idfilec, comprobante, nombre, tipo FROM filec WHERE idfilec = %s", (new_id,))
    filec_record = cursor.fetchone()


    if filec_record is None:
        raise HTTPException(status_code=500, detail="Failed to create the filec record")

    # Crea un objeto Filec y lo devuelve como respuesta
    idfilec, comprobante, nombre, tipo = filec_record
    filec = Filec(idfilec=idfilec, comprobante=comprobante, nombre=nombre, tipo=tipo)
    return filec


@app.get("/get_file2/", response_model=List[File2])
def get_file_2(request: Request):

    # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # The token is valid, get the list of file2

    cursor.execute("SELECT * FROM file2")
    users_data = cursor.fetchall()
    file2 = [User(idfile2=idfile2, cuenta=cuenta, nombre=nombre, naturaleza=naturaleza) for idfile2, cuenta, nombre, naturaleza in users_data]
    return file2


@app.get("/get_file1/", response_model=List[File1])
def get_file1(request: Request):

    # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # The token is valid, get the list of file1

    cursor.execute("SELECT * FROM file1")
    users_data = cursor.fetchall()

    file1 = [User(id_comprobante=id_comprobante, fecha_documento=fecha_documento, documento=documento, id_cuenta=id_cuenta,id_cedula=id_cedula,id_c_costos=id_c_costos, factura=factura, valor=valor, tipo=tipo, concepto=concepto, fecha_insert=fecha_insert, fecha_update=fecha_update) for idFile1, id_comprobante, fecha_documento, documento, id_cuenta, id_cedula, id_c_costos, factura, valor, tipo, concepto, fecha_insert, fecha_update in users_data]
    return file1


@app.get("/users/", response_model=List[User])
def get_users(request: Request):
    """
    Get a list of users.

    Args:
        request: FastAPI Request object for receiving the user's token.

    Returns:
        A list of User objects.
    """
    # Verify the provided token
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
    user_email = cursor.fetchone()

    if user_email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # The token is valid, get the list of users
    cursor.execute("SELECT id, name, email, token FROM users")
    users_data = cursor.fetchall()

    users = [User(id=id, name=name, email=email, token=token) for id, email, name, token in users_data]
    return users





def user_exists(user_id: int) -> bool:
    """
    Check if a user exists in the database.

    Args:
        user_id: The ID of the user to check.

    Returns:
        `True` if the user exists, `False` otherwise.
    """
    cursor.execute("SELECT id FROM user WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    return user is not None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
