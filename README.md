```
      _---~~~(~~~-_.
    _{         )     )
  ,   ) -~~-- (   ,,-' )_
 (  `-,_..`., ')----- '_,).      ___     __  __        __  __     +            ___       ___      
( ` _)  (  -~( --__-__ `,  }    |__ |\/|/  \|__)\ /   |__)|__) /\ ||\ |   |__||__  /\ |   ||__| 
(_-  _  ~_-~~~~~~~`,-- ,' ).    |___|  |\__/|  \ |    |__)|  \/~~\|| \|   |  ||___/~~\|___||  | 
  `~ -^(    _____;-,((())).     _______________________________________________________________
       ~~~~~~ {_ -_(())
               `\  }
                 { } 
```

# gindata-image-processing

This repository will be used to define build specifications for containerized images that outline image processing steps that are available to execute against Gindata imaging data.

## Available Images:

### 1. Convert Magnetic Resonance Imaging (MRI) brain imaging data from DICOM format to NIfTI format and organize in the BIDS output structure

This image processing unit is supplied in the form of a Docker container available to convert MRI brain imaging data to the Neuroimaging Informatics Technology Initiative (NIfTI) open file format  Brain Imaging Data Structure) A simple and intuitive way to organize and describe your neuroimaging and behavioral data.

More details on [`dicom_to_nifti`](./src/dicom_to_nifti/README.md) container

### 2. [STATUS - PLANNED]: Perform brain image segmentation using fastsurfer and derive volumetric data points

More details on [`fastsurfer_volumetrics`](./src/fastsurfer_volumetrics/README.md) container

![](./medical.png)



