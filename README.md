# AVAT_img_conversion

This script is designed to convert generated annotations from the AVAT (https://github.com/AIFARMS/AVAT) into image format.

## Installation

This project uses python3, pip and venv. Please install them based off of your system requirements.

Setup virtual env:
```
python3 -m venv vir_env
```

Setup terminal to virtual environment:
```
source vir_env/bin/activate
```

Install dependencies:
```
pip3 install -r requirements.txt
```

## Usage

There are a few inputs needed to the app to function, you will need a video file and the annotation file generated by AVAT. 

```
python3 -i <INPUT FILE PATH> -s <FRAME SKIP VALUE> -a <ANNOTATION FILE PATH>
```

A sample input would be:

```
python3 main.py -i /home/test_user/Desktop/video.mp4 -s 15 -a /tmp/generated_annotations-1.json
```

## TODO
* [ ] Support for segmentation annotations
* [ ] More customizable options for output files
* [ ] Custom post processing scripts