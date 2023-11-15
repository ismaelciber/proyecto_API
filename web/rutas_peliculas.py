from flask import request, session
import json
import decimal
from __main__ import app
import controlador_peliculas

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/peliculas",methods=["GET"])
def peliculas():
    peliculas,code= controlador_peliculas.obtener_peliculas()
    return json.dumps(peliculas, cls = Encoder),code

@app.route("/pelicula/<id>",methods=["GET"])
def pelicula_por_id(id):
    pelicula,code = controlador_peliculas.obtener_pelicula_por_id(id)
    return json.dumps(pelicula, cls = Encoder),code

@app.route("/peliculas",methods=["POST"])
def guardar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        ret,code=controlador_peliculas.insertar_pelicula(pelicula_json["nombre"], pelicula_json["descripcion"], int(pelicula_json["fecha"]), pelicula_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/peliculas/<id>", methods=["DELETE"])
def eliminar_pelicula(id):
    ret,code=controlador_peliculas.eliminar_pelicula(id)
    return json.dumps(ret), code

@app.route("/peliculas", methods=["PUT"])
def actualizar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        ret,code=controlador_peliculas.actualizar_pelicula(pelicula_json["id"],pelicula_json["nombre"], pelicula_json["descripcion"], int(pelicula_json["fecha"]),pelicula_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code