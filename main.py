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
    FilecCreate
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

# @app.get("/get_file1/", response_model=List[File1])
# def get_file1(request: Request):

#     # Verify the provided token
#     token = request.headers.get("Authorization")
#     if not token:
#         raise HTTPException(status_code=401, detail="No token provided")
#     cursor.execute("SELECT email FROM users WHERE token = %s", (token,))
#     user_email = cursor.fetchone()

#     if user_email is None:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     # The token is valid, get the list of file1

#     cursor.execute("SELECT * FROM file1")
#     users_data = cursor.fetchall()

#     file1 = [User(id_comprobante=id_comprobante, fecha_documento=fecha_documento, documento=email, token=token) for id, email, name, token in users_data]
#     return file1


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




# @app.post("/create_project/", response_model=create_Project)
# def create_project(request: Request, project: create_Project):
#     """
#     Create a new project.

#     Args:
#         request: FastAPI Request object for receiving the user's token.
#         project: create_Project object containing project data.

#     Returns:
#         The newly created create_Project object.
#     """
#     # Verify the provided token
#     token = request.headers.get("Authorization")
#     if not token:
#         raise HTTPException(status_code=401, detail="No token provided")

#     cursor.execute("SELECT email FROM user WHERE token = %s", (token,))
#     user_email = cursor.fetchone()

#     if user_email is None:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     # Verify that the customer ID exists in the customers table
#     cursor.execute("SELECT id FROM customer WHERE id = %s", (project.customer_id,))
#     customer = cursor.fetchone()

#     # Create the user if it doesn't exist
#     if not user_exists(project.created_by_user_id):
#         cursor.execute("INSERT INTO user (id) VALUES (%s)", (project.created_by_user_id,))
#         cursor.connection.commit()

#     if customer is None:
#         raise HTTPException(status_code=400, detail="Invalid customer ID")

#     # Verify that the created_by_user_id exists in the users table
#     cursor.execute("SELECT id FROM user WHERE id = %s", (project.created_by_user_id,))
#     user = cursor.fetchone()

#     if user is None:
#         raise HTTPException(status_code=400, detail="Invalid created_by_user_id")

#     project.useridentifier = 1
#     # The token is valid, you can add a new project to the database
#     cursor.execute("""
#         INSERT INTO project (name, address, customer_id, city, state, zipcode, stage, tenant_id, datecreated, country, address_2, updated_on_date, created_by_user_id, domotz_agent_id, customer_location_id, updated_by_user_id, teams_url, planner_url, enable_teams_url)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#         project.name,
#         project.address,
#         project.customer_id,
#         project.city,
#         project.state,
#         project.zipcode,
#         project.stage,
#         project.tenant_id,
#         project.datecreated,
#         project.country,
#         project.address_2,
#         project.updated_on_date,
#         project.created_by_user_id,
#         project.domotz_agent_id,
#         project.customer_location_id,
#         project.updated_by_user_id,
#         project.teams_url,
#         project.planner_url,
#         project.enable_teams_url
#     ))

    # Make sure to commit the changes to the database
    connection.commit()

    # Return the newly created project
    return project

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
