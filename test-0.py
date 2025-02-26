from qgis.core import QgsRasterLayer
from PyQt5.QtCore import QFileInfo

def StringToRaster(raster):
    # Check if string is provided

    fileInfo = QFileInfo(raster)
    path = fileInfo.filePath()
    baseName = fileInfo.baseName()

    layer = QgsRasterLayer(path, baseName)
    QgsProject.instance().addMapLayer(layer)

    if layer.isValid() is True:
        print ("Layer was loaded successfully!")

    else:
        print ("Unable to read basename and file path - Your string is probably invalid")

tile_dsm = "/media/ljp238/12TBWolf/RSPROX/OUT_TILES/BLOCKS/TLS/DOWNX/DSM/tiles/N13E103_DTM_GV4.tif"
StringToRaster(tile_dsm)

