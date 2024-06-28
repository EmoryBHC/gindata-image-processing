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

## Available Processing Container Images:

### 1. Convert Magnetic Resonance Imaging (MRI) brain imaging data from DICOM format to NIfTI format and organize in the BIDS output structure

This image processing unit is supplied by CN2L in the form of a Docker container that is able to be built and executed to convert MRI brain imaging data in DICOM format to the Neuroimaging Informatics Technology Initiative (NIfTI) open file format, as well as organizing the output in the Brain Imaging Data Structure (BIDS). 

More details on [`dicom_to_nifti`](./src/dicom_to_nifti/README.md) container

### 2. [STATUS - PLANNED]: Perform brain image segmentation using fastsurfer and derive volumetric data points

This image processing unit is planned to be supplied by CN2L and will allow derivation of fastsurfer volumetrics data, as well as segmentation data.

More details on [`fastsurfer_volumetrics`](./src/fastsurfer_volumetrics/README.md) container

## Gindata Image Processing Output 

TBD - The output of containerized image processing pipelines will be added to the Gindata image inventory data, to ensure that structured output data is queryable alongside image metadata.

<!-- ROADMAP -->
## Roadmap

- [x] Validate dicom_to_nifti image conversion
- [ ] Develop approach to organize execution of dicom_to_nifti image conversion on Gindata image inventory
- [ ] Supply images to external collaborators
- [ ] Execute containerized image processing against Gindata image inventory & save output as structured data
- [ ] Develop further containerized image processing units
    - [ ] Work with researchers and external collaborators to understand future needs
    - [ ] Other functionality of interest

<!-- LICENSE -->
## License

Distributed under the TBD License. See [`LICENSE.txt`](LICENSE.txt) for more information.

<!-- CONTACT -->
## Contact

For more information, please contact Gindata Operations at gindata@emory.edu.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Containerized images for performing image processing operations are developed and supplied by the CN2L lab, and will be in use in the Gindata data lake in the future to process ingested imaging data.

* [Computational NeuroImaging & Neuroscience Lab](https://randomprogram.net/)

![](./medical.png)
