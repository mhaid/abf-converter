# ABF-converter
Conversion of ABF files to make them compatible with the mini analysis program

## Description
This python script convertes ABF files (Axon™ Binary File Format) with any ABF file version supported by pyABF into
the compatible version for Mini Analysis Program (ABF Version 1).

## Usage
1. Clone the repository
2. Install all Prerequisites
   - [Python 3](https://www.python.org/downloads/) (Python 3.6+)
   - [pyABF](https://swharden.com/pyabf/tutorial/)
5. Place all ABF files you wish to make compatible with the Mini Analysis Program into the folder _input_.
6. Start the python script (if you use windows, simply open the file "run.bat"). The script will now convert all .abf files located in the _input_ folder.
8. The compatible output files will be saved into the folder _output_.

## Licence
This script can be used following the MIT Licence.

## Acknowledgments
This script is based on [pyABF by SW Harden (MIT Licence)](https://pypi.org/project/pyabf/).

The ABF format is outlined by [Molecular Devices](https://mdc.custhelp.com/euf/assets/software/FSP_ABFHelp_2.03.pdf).
