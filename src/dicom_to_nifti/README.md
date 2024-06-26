
# DICOM to NIfTI Conversion

## Image Processing Available with this image:

## Example:

`docker build -t heudiconv-from-repo:v1 .`

`docker run -v <INPUT MAPPING> -v <OUTPUT MAPPING> heudiconv-from-repo:v1 -d "/src/heudiconv/dicom-anon/{subject}/{session}/*/*.dcm" -o /src/heudiconv/bids-nifti -f /src/heudiconv/heuristic.py -s "<>" -ss "<>" -c dcm2niix --bids --overwrite`

^  Important to use quotes around the -d flag input

## Usage

## Flags

-d 
-files
 ... etc.
