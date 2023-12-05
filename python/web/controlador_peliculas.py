from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_pelicula(nombre, descripcion, fecha,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas(nombre, descripcion, fecha,foto) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, fecha,foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar una pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id'] = pelicula[0]
    d['nombre'] = pelicula[1]
    d['descripcion'] = pelicula[2]
    d['fecha'] = pelicula[3]
    d['foto'] = pelicula[4]
    return d

def obtener_peliculas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, fecha,foto FROM peliculas")
            peliculas = cursor.fetchall()
            peliculasjson=[]
            if peliculas:
                for pelicula in peliculas:
                    peliculasjson.append(convertir_pelicula_a_json(pelicula))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener las peliculas", file=sys.stdout)
        peliculasjson=[]
        code=500
    return peliculasjson,code

def obtener_pelicula_por_id(id):
    peliculajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, fecha,foto FROM peliculas WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, descripcion, fecha,foto FROM peliculas WHERE id =" + id)
            pelicula = cursor.fetchone()
            if pelicula is not None:
                peliculajson = convertir_pelicula_a_json(pelicula)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar una pelicula", file=sys.stdout)
        code=500
    return peliculajson,code


def eliminar_pelicula(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar una pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_pelicula(id, nombre, descripcion, fecha, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE peliculas SET nombre = %s, descripcion = %s, fecha = %s, foto=%s WHERE id = %s",
                       (nombre, descripcion, fecha, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar una pelicula", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
