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


if __name__ == '__main__':
    # Path of this script
    path_here = os.path.dirname(__file__)
    
    # One directory up from the location of this script
    path_start, _ = os.path.split(os.path.dirname(__file__))
    
    # Directory to move to
    PDF_DIR = 'alle_pdf_filer'
    FAGKODER = {'1P', '2P', '1T', 'S1', 'S2', 'R1', 'R2', '2T'}
    
    shutil.rmtree(os.path.join(path_start, PDF_DIR))
    os.makedirs(os.path.join(path_start, PDF_DIR), exist_ok=True)
    
    # Regex pattern
    fagkoder_joined = '|'.join((f for f in FAGKODER))
    pattern_str = r'(' + fagkoder_joined + r')\_\d{2}(H|V).{0,3}\.pdf'
    pattern = re.compile(pattern_str)
    
    for dirpath, dirnames, filenames in os.walk(path_start):
        
        # Skip the .git folder
        if ('.git' in dirpath) or (PDF_DIR in dirpath):
            continue
        
        # For every filename
        for filename in filenames:
            
            # If the filename does not match the pattern, skip it
            if not pattern.match(filename):
                continue
            
            # The filename matched the pattern, keep going
            copy_from = os.path.join(dirpath, filename)
            copy_to = os.path.join(path_start, PDF_DIR, filename)
            shutil.copy2(copy_from, copy_to)
            print('Copied to:', copy_to)