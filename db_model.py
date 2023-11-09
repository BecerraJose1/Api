# model.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Union

class LoginRequest(BaseModel):
    """
    Represents a request to login.

    Args:
        email (str): The email address of the user trying to login.
        password (str): The password of the user trying to login.
    """

    email: str
    password: str

class LoginResponse(BaseModel):
    """
    Represents the response received after a successful login attempt.

    Attributes:
        token (str): The authentication token received after a successful login attempt.
    """

    token: str

class User(BaseModel):
    """
    Represents a user in the system.

    Attributes:
        id (int): The ID of the user.
        email (str): The email address of the user.
    """

    id: int
    email: str
    name: str
    token:str

class FilecCreate(BaseModel):
    comprobante: str
    nombre: str
    tipo: str


class File1Create(BaseModel):
    id_comprobante: Union[int, None]
    fecha_documento: Union[datetime, None]
    documento: Union[int, None]
    id_cuenta: Union[int, None]
    id_cedula: Union[int, None]
    id_c_costos: Union[int, None]
    factura: Union[str, None]
    valor: Union[int, None]
    tipo: Union[int, None]
    concepto: Union[str, None]
    fecha_insert: Union[datetime, None]
    fecha_update: Union[datetime, None]

class File1(BaseModel):
    idFile1: Union[int, None]
    id_comprobante: Union[int, None]
    fecha_documento: Union[datetime, None]
    documento: Union[datetime, None]
    id_cuenta: Union[int, None]
    id_cedula: Union[int, None]
    id_c_costos: Union[int, None]
    factura: Union[str, None]
    valor: Union[int, None]
    tipo: Union[int, None]
    concepto: Union[str, None]
    fecha_insert: Union[datetime, None]
    fecha_update: Union[datetime, None]


class File2(BaseModel):
    idfile2: Union[int, None]
    cuenta: Union[int, None]
    nombre: Union[str, None]
    naturaleza: Union[str, None]

class File3(BaseModel):
    idfile3: Union[int, None]
    cedula: Union[int, None]
    nombre1: Union[str, None]
    nombre2: Union[str, None]
    apellido1: Union[str, None]
    apellido2: Union[str, None]
    direccion: Union[str, None]
    celular: Union[str, None]
    correo: Union[str, None]
    id_ciudad: Union[int, None]
    tipo_cedula: Union[int,None]


class File3Create(BaseModel):
    cedula: Union[int, None]
    nombre1: Union[str, None]
    nombre2: Union[str, None]
    apellido1: Union[str, None]
    apellido2: Union[str, None]
    direccion: Union[str, None]
    celular: Union[str, None]
    correo: Union[str, None]
    id_ciudad: Union[int, None]
    tipo_cedula: Union[int,None]


class File_ciudad(BaseModel):
    idfile_ciudad: int
    nombre_ciudad: str

class Filec(BaseModel):

    idfilec:int
    comprobante:str
    nombre:str
    tipo:int



