import BigWorld
import json
import os
from gui.Scaleform.daapi.view.meta.TankCarouselMeta import TankCarouselMeta

# Mod info
__author__ = 'SteelPhoenix'
__version__ = 'v1.0'
__prefix__ = '[CarouselMod]'

print(__prefix__ + ' Loading ' + __name__ + ' ' + __version__ + ' by ' + __author__ + '...')

rows = 5

# Function swap
old_func = TankCarouselMeta.as_rowCountS

def new_func(self, value):
    old_func(self, value)
    if self._isDAAPIInited():
        return self.flashObject.as_rowCount(rows)

TankCarouselMeta.as_rowCountS = new_func

# If a config file exists
if os.path.exists('mods/configs/SPCarousel/config.json'):
    print(__prefix__ + ' Found existing config file')
    with open('mods/configs/SPCarousel/config.json') as file:
        data = json.load(file)

        if 'rows' in data:
        	value = data['rows']
        	if type(value) == int and value >= 1:
        		rows = value
       		else:
       			print(__prefix__ + ' The \'rows\' value needs to be a positive integer, found: ' + str(value))
        else:
        	print(__prefix__ + ' Config file does not contain \'rows\', using default value ' + str(value))
else:
    print(__prefix__ + ' Creating config file')

    # Create config directory if it does not exist
    if not os.path.exists('mods/configs/SPCarousel'):
        os.makedirs('mods/configs/SPCarousel')

    # Write defaults
    with open('mods/configs/SPCarousel/config.json', 'w') as file:
        json.dump({'rows': rows}, file, separators = (',', ': '), indent = 4)
        file.write('\n')

print(__prefix__ + ' Rows: ' + str(rows))