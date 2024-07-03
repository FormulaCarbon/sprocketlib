# SprocketLib
Sprocket Blueprint Loading Library

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
partsAndProperties = bp.load_blueprints_properties()                          # Loads all properties of each part. Must be called after bp.load_blueprints()
```
