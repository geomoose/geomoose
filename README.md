This is the readme file for GeoMOOSE MS4W package.  If you haven't installed
this application yet, please read the approriate INSTALL file for installation
instructions.

This directory contains the following files and subdirectories:

     LICENSE
           -   this is the legal notice from the GeoMOOSE project

     README.txt
           -   This file.

     art   -   this directory contains the original graphics designed for
               the GeoMOOSE project. This directory is not web accessible.

     conf    - this directory contains the GeoMOOSE configuration files and is not web accessible.


     htdocs - this directory is where all web-readable files and
               subdirectories are located.  This is the directory that is
               referenced in Apache's Alias or Microsoft IIS's virtual directory.
               This folder contains the GeoMOOSE and Openlayers code along with the graphic images
               that make the user interface.


     maps    - this directory contains the data layers used by the
               GeoMOOSE demo application.  All datasets and MapServer mapfiles
               are contained in this directory.  This is not a web accessible
               directory.
               
     sphinx-docs  - this directory contains the scripts and documents to build a html version of documentation.

     tools -   this directory contains the scripts
               needed to "build" or "combine and compress" the individual javascript and css files into one GeoMOOSE.js library.  These scripts were adapted from the OpenLayers project (www.openlayers.org).
               These scripts require knowledge of python and are primarily only useful for developers who a modifying the javascript source code.
               These script have not been tested thourghly, so please use with caution.

You can checkout the full source code with your choice of:

```
git clone --recursive git://github.com/geomoose/geomoose.git
git clone --recursive git@github.com:geomoose/geomoose.git
git clone --recursive https://github.com/geomoose/geomoose.git
```
