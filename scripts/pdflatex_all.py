#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kopierer alle .pdf filer som matcher følgende mønster:

(FAGKODE)_(2 TALL)_(V eller H)_(1-3 bokstaver)_(.pdf)

Til en egen mappe.
@author: tommy
"""

import os
import re
import shutil
import zipfile
import subprocess


if __name__ == '__main__':
    # Path of this script
    path_here, _ = os.path.split(os.path.realpath(__file__))
    
    # One directory up from the location of this script
    path_start, _ = os.path.split(path_here)
    
    # Pattern for filene
    FAGKODER = {'1P', '2P', '1T', 'S1', 'S2', 'R1', 'R2', '2T'}
    fagkoder_joined = '|'.join((f for f in FAGKODER))
    pattern_str = r'(' + fagkoder_joined + r')\_\d{2}(H|V).{0,3}\.tex'
    pattern = re.compile(pattern_str)
    
    for dirpath, dirnames, filenames in os.walk(path_start):
        for filename in filenames:
            fname_no_ext, ext = os.path.splitext(filename)
            
            if ext != '.tex':
                continue
            
            # If the filename does not match the pattern, skip it
            if not pattern.match(filename):
                continue
            
            # Change directory, run latex, delete files
            os.chdir(dirpath)    
            args = ['pdflatex',
                    '-synctex=1',
                    '-interaction=nonstopmode',
                    filename]
            
            # Bruk pdflatex på filen
            subprocess.check_call(args, cwd=dirpath, stdout=subprocess.DEVNULL)
            print('{} -> {}'.format(filename, filename.replace('.tex', '.pdf')))
 
    