from distutils.core import setup 
import py2exe 
 
setup(name="printFile", 
 version="0.0.1", 
 description="File Print", 
 author="Carlos Vasquez", 
 author_email="virahondacarlos@gmail.com",
 license="MIT License", 
 scripts=["printFile.py"],
 console=["printFile.py"],
 zipfile=None,
)