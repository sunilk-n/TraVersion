# TraVersion
TraVersion is similar way of maintaining semantic versioning in python, where the major points are introduced in this repository.

####Note:
The word TraVersion is taken from Traverse which means  "to go or travel across or over"

###Usage Example:
* Default version
    ``` python
    from traVer import Version
    version = Version()
    
    # Default version will be 1.0.0
    print(version) >>> 1.0.0 
    ```
* Assigning version
    ``` python
  from traVer import Version
  version = Version("2.3.4-beta.5")
  
  # You can specify major, minor, patch, preRelName, preRelease
  print(version.major) >>> 2
  print(version.patch) >>> 4
  ```
