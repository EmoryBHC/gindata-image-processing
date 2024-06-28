
# DICOM to NIfTI Conversion

## Image Processing Available with this image
Description

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Example Usage

`docker build -t dicom_to_nifti .`

`docker run -v <INPUT MAPPING> -v <OUTPUT MAPPING> dicom_to_nifti -d "<MAPPED FILE INPUT>/{subject}/{session}/*/*.dcm" -o /src/heudiconv/bids-nifti -f /src/heudiconv/heuristic.py -s "<>" -ss "<>" -c dcm2niix --bids --overwrite`

* Important to use quotes around the -d flag input

## Flag Options 

-d 
-files
 ... etc.

## 

https://heudiconv.readthedocs.io/en/latest/
