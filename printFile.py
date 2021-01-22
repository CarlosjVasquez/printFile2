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
    name = request.args.get('name')
    destino ='C:/Users/USUARIO/Desktop/Trabajo/ProyectoLibertad/printFile/pdf/' + str(username)
    if not os.path.exists(destino):
        os.makedirs(destino)
    namefinish = destino+ '/' + str(name) + '.pdf'
    download = wget.download(url, namefinish)

    return download



@app.route("/print/",methods=['GET'])
def print():

    name = request.args.get('name')
    username = request.args.get('username')

    url = 'C:\\Users\\USUARIO\\Desktop\\Trabajo\\ProyectoLibertad\\printFile\\pdf\\' + str(username) +'\\' + str(name) + '.pdf'

    return_code = subprocess.call(["PDFtoPrinter", url ,"PDFCreator"], shell=True) 

    if(return_code != 0):
        return 'Error'
    else: 
        return url
        

if __name__ == "__main__":
    app.run(host='localhost',
            debug=True,
            port=8080)


