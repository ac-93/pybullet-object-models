import os
from glob import glob

def getDataPath():
  resdir = os.path.join(os.path.dirname(__file__))
  return resdir

def getLayoutList():
    data_path = getDataPath()
    model_list = [y for x in os.walk(data_path) for y in glob(os.path.join(x[0], '*.sdf'))]
    try:
        model_list.remove('__pycache__')
    except:pass
    return model_list
