# python_image_examples
Example images for image processing, packaged for Python

## Data
* 'Miscellaneous' volume of images from USC SIPI: http://sipi.usc.edu/database/database.php?volume=misc
* Shepp-Logan phantom - Wikimedia rendering: https://commons.wikimedia.org/wiki/File:Shepp_logan.png
* 'Cameraman' B&W photo, taken from https://www.hlevkin.com/TestImages/

## Usage
Images can be loaded using an alias:
>>> from image_examples import peppers

The object loaded has several properties, including the filename for loading the data yourself:
>>> peppers.filename # doctest:+ELLIPSIS
'...\\image_examples\\data\\usc_misc\\4.2.07.tiff'
