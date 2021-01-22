#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

import subprocess

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("form.html")

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


