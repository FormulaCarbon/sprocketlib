# SprocketLib
Sprocket Blueprint Loading Library

## Usage
```py
import sprocketlib as sp

bpData = sp.base.parse_blueprint("path/to/file") # Load blueprint from file as dict
bpData_fromString = sp.base.parse_blueprint("blueprint text", rawText = True) # Load blueprint from string as dict
```
