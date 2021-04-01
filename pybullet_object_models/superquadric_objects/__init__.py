import os


def getDataPath():
  resdir = os.path.join(os.path.dirname(__file__))
  return resdir

def getModelList():
    data_path = getDataPath()
    model_list = [os.path.basename(os.path.normpath(f.path)) for f in os.scandir(data_path) if f.is_dir()]
    try:
        model_list.remove('__pycache__')
    except:pass
    return model_list

