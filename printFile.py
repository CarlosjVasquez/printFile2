#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

import subprocess
import wget
import os

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def Hello():
    return 'Hola'

@app.route("/download/", methods=['GET'])
def download():

    url = request.args.get('url')
    username = request.args.get('username')
    destino ='C:/Users/USUARIO/Desktop/Trabajo/ProyectoLibertad/printFile/pdf/' + str(username)
    if not os.path.exists(destino):
        os.makedirs(destino)
    download = wget.download(url, destino)

    return download



@app.route("/print/<nombre>",methods=['GET'])
def print(nombre):

    return_code = subprocess.call(["PDFtoPrinter", nombre ,"PDFCreator"], shell=True) 

    if(return_code != 0):
        return 'Error'
    else: 
        return 'Ok'
        

if __name__ == "__main__":
    app.run(host='localhost',
            debug=True,
            port=8080)


