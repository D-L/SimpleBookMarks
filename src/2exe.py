from distutils.core import setup
import py2exe
options={
    "py2exe":{
        "compressed": 1,
        "bundle_files": 1
    }
}
setup(     
    options = options,      
    zipfile=None,
    console=[{"script": "simple.py", "icon_resources": [(1, "static\\favicon.ico")] }]
    )
