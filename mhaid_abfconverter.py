#!/usr/bin/env python
"""Conversion of ABF files of any supported version into ABF files that are compatible with the Mini Analysis Program

Description:
This python script convertes ABF files with any ABF file version supported by pyABF into
the compatible version for Mini Analysis Program (ABF Version 1).

Further information:
ABF File format -> https://mdc.custhelp.com/euf/assets/software/FSP_ABFHelp_2.03.pdf
pyABF Website   -> https://swharden.com/pyabf/

Tested with:
Python        -> Version 3.10.12
pyABF Python  -> Version 2.3.8

Licence
MIT License

Copyright (c) 2024 Morris Haid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import pyabf


__author__ = "Morris Haid"
__copyright__ = "Copyright 2024"
__credits__ = ["Morris Haid"]
__license__ = "MIT License"
__version__ = "0.1.1"
__maintainer__ = "Morris Haid"
__email__ = "morris.haid@hhu.de"
__status__ = "Prototype"

# Constants for File Directory
INPUT_DIR = os.path.abspath(os.path.dirname(__file__))+"/input/" # Use directory of script
OUTPUT_DIR = os.path.abspath(os.path.dirname(__file__))+"/output/" # Use directory of script


print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
print( '---{: ^65}---'.format(">>> ABF File Conversion <<<") )
print( '---{: ^65}---'.format("for usage of .abf with 'Mini Analysis Program'") )
print( '---{: ^65}---'.format("Version "+__version__) )
print( '---{: ^65}---'.format("by "+__author__) )
print( '---{: ^65}---'.format("Licence: "+__license__) )
print( '---{: ^65}---'.format("Status: "+__status__) )
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
print("")
print("")

# --------------- Helper Functions ---------------
def do_abf_conversion(filename):

    # Open ABF file 
    abf = pyabf.ABF(INPUT_DIR+filename)
    abf.saveABF1(OUTPUT_DIR+filename)


# --------------- STEP 0: Setup file directory ---------------
# check if neccessary directories exist

# --------------- STEP 1: Fetch available regions in space and parcellation ---------------
print("Start conversion of .abf files")
print("Locating files in "+INPUT_DIR)
filesconverted_cnt = 0

for filename in os.listdir( INPUT_DIR ):
    
    print("----------")

    if filename.endswith(".abf"):
        print("Converting "+filename+"...")
        do_abf_conversion(filename)
        print("Done converting "+filename)
        filesconverted_cnt += 1
    else:
        print("Skipping conversion of "+filename+" due to incompatible format.")


print("----------")
print("")
print("Processed all files in the directory '"+OUTPUT_DIR+"'.")
print("Converted "+str(filesconverted_cnt)+" files.")
print("")
print("Thanks for using.")
print("Have a good day!")
print("")
print('{: ^15}'.format("/\\_/\\") )
print('{: ^15}'.format("( o.o )") )
print('{: ^15}'.format("> ^ <") )
print("")