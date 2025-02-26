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
