# EggPy (previously EXG)
 
 The EggPy Package handles Electrophysiological Time-Series Data to do the following:
  - Read Data from Common File Types
  - Crop Data
  - Bandpass Filter Data
  - Fast-Fourier Transform Data
  - Plot Data (in the Time and Frequency Domain)


# How to Use EggPy:

## Read Data from Common File Types
 Pre-requisites:
*************************************
To read a file, you will need to have a file to read, such as an OpenBCI-your-file-name.txt file. This document assumes your files are in the same directory as where you are running your script with EggPy. 
*************************************
Notes:
*************************************
Currently only supports OpenBCI.txt files.
*************************************
 
 1. Import a session object from EggPy
 2. Create/Assign a session object to a variable (reffered to as S1 in this documet)
    - One Required Argument: 'your-file-name.txt'
 3. 
