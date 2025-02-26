import os 
from glob import glob 
#rom qrloader import StringToRaster

from qgis.core import QgsRasterLayer
from PyQt5.QtCore import QFileInfo

def StringToRaster(raster, display_name=None):
    # Check if string is provided
    fileInfo = QFileInfo(raster)
    path = fileInfo.filePath()
    baseName = fileInfo.baseName()

    # Use the provided display_name if available, otherwise use the baseName
    layer_name = display_name if display_name else baseName

    # Create the raster layer with the specified display name
    layer = QgsRasterLayer(path, layer_name)

    # Add the layer to the QGIS project
    QgsProject.instance().addMapLayer(layer)

    # Check if the layer was loaded successfully
    if layer.isValid():
        print(f"Layer '{layer_name}' was loaded successfully!")
    else:
        print("Unable to read basename and file path - Your string is probably invalid")



path = "/media/ljp238/12TBWolf/ARCHIEVE/FABDEM/data/"
files = glob(f'{path}/*/*.tif'); print(len(files))

tilenames = ['N10E105', 'N13E103','S01W063']
tilestiles = [i for i in files for t in tilenames if t in i]
tilestiles

assert len(tilestiles) == len(tilenames), 'Length !='

for fi in tilestiles:
    print(fi)
    StringToRaster(fi)



