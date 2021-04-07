import os, sys

def getDataPath():
  resdir = os.path.join(os.path.dirname(__file__))
  subdirs_exist = any(os.path.isdir(os.path.join(resdir, i)) for i in os.listdir(resdir) if i != '__pycache__')
  if not subdirs_exist:
      sys.exit('Warning, no models exist for object set located ({}). Check they are dowloaded correctly.'.format(resdir))
  return resdir

def getModelList():
    data_path = getDataPath()
    model_list = [os.path.basename(os.path.normpath(f.path)) for f in os.scandir(data_path) if f.is_dir()]
    try:
        model_list.remove('__pycache__')
    except:pass
    return model_list

def getMeshStr():
    return "{filename}/{filename}.obj"

def getURDFStr():
    return "{filename}/model.urdf"

def getURDFScale():
    return [1.0, 1.0, 1.0] 
