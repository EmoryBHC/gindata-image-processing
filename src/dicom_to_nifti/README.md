
# DICOM to NIfTI Conversion

## Image Processing Available with this image
A flexible DICOM converter for organizing brain imaging data into structured directory layouts by converting brain MRI imaging data in DICOM format to NIfTI format and providing output in the BIDS format. 

This image processing unit was created by the Computational NeuroImaging & Neuroscience Lab (CN2L) in the form of a Docker container available to convert MRI brain imaging data to the Neuroimaging Informatics Technology Initiative (NIfTI) open file format and storing it in the Brain Imaging Data Structure (BIDS). A simple and intuitive way to organize and describe your neuroimaging and behavioral data.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* docker
* Brain MRI imaging data in DICOM format

### Installation & Example Usage

_Follow these steps to build the container image and get started :_

1. Clone the repo
   ```sh
   git clone https://github.com/EmoryBHC/gindata-image-processing.git
   ```
3. Build the docker container 
   ```sh
   docker build -t dicom_to_nifti .
   ```
4. Run the conversion process by running the docker container with image data input. Please note the use of quotes around the -d flag input
   ```sh
  docker run -v <INPUT MAPPING> -v <OUTPUT MAPPING> dicom_to_nifti -d "<MAPPED FILE INPUT>/{subject}/{session}/*/*.dcm" -o /src/heudiconv/bids-nifti -f /src/heudiconv/heuristic.py -s "<SUBJECT ID>" -ss "<SESSION ID>" -c dcm2niix --bids --overwrite
   ```

## Flag Options 

-d 
-files

## More Information about Base Libraries

a. heudiconv : [https://heudiconv.readthedocs.io/en/latest/](https://heudiconv.readthedocs.io/en/latest/)
b. dcm2niix : 
