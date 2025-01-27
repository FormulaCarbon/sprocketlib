# SprocketLib
Sprocket Blueprint Loading Library

## Installation

```bash
pip install -i https://test.pypi.org/simple/ sprocketlib
```
## Limitations
As of version 0.1.0, sprocketlib can load only sub-blueprints, not meshes. mesh loading is currently in the works.

## Usage
```py
import sprocketlib as sp

bpData = sp.base.parse_blueprint("path/to/file")                              # Load blueprint file as dict
bpData_fromString = sp.base.parse_blueprint("blueprint text", rawText = True) # Load blueprint string as dict

bp = sp.base.BluePrint("path/to/file")                                        # Load blueprint file as BluePrint Object
header = bp.get_header()                                                      # Returns header as dict
partID = bp.get_part_id("compartment name", "compartment type")               # Returns ID of part given name and type, eg. "compartment1" and "Compartment"
blueprints = bp.get_blueprints()                                              # Returns all part sub-blueprints as a list of dicts
parts = bp.load_blueprints()                                                  # Loads all sub-blueprints as part objects as defined in sprocketlib.parts. Saves to bp.blueprints. Returns a list of part objects
partsAndProperties = bp.load_blueprints_properties()                          # Loads all properties of each part. Must be called after bp.load_blueprints(). updates bp.blueprints
```

### Quickstart
```py
from sprocketlib.base import *

BLUEPRINT = "path/to/blueprint.blueprint"

vehicle = BluePrint(BLUEPRINT)
vehicle.load_blueprints()
vehicle.load_blueprints_properties()

for part in vehicle.blueprints:
    print(part.name, part.type, part.id)
```

## TODO
- Finish mesh implementation
- Write documentation for mesh
- Write more example code
- Write tests
- Optimize ID search and part loading
- Replace lists with numpy arrays

## Building
py -m setup sdist bdist_wheel
twine upload --repository testpypi dist/*
