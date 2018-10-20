#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kjører pdflatex på alle .tex filer som matcher følgende mønster:
    
(FAGKODE)_(2 TALL)_(V eller H)_(1-3 bokstaver)_(.tex)

@author: tommy
"""

import os
import re
import subprocess
import hashlib
import time

def hash_file(file_path):
    """
    Return the hash of a file.
    """
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        md5.update(file.read())
        
    return md5.hexdigest()

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
            
            print(f'-------- {filename} --------')
            time.sleep(0.1)
            
            # Print full file path
            hashed_filename = os.path.join(dirpath, filename).replace('.tex', '.hash')
            tex_hashed = hash_file(os.path.join(dirpath, filename))
            try:
                with open(hashed_filename, 'r') as hashed_file:
                    if hashed_file.read().strip() == tex_hashed:
                        print('Same hash - file has not been updated.')
                        continue
                    else:
                        print('Different hash - file has been updated.')
                        print('Stored hash:', hashed_file.read().strip())
                        print('New hash:   ', tex_hashed)
                        
            except FileNotFoundError:
                with open(hashed_filename, 'w') as hashed_file:
                    print('Hash file not found. Writing.')
                    hashed_file.write(tex_hashed)
                    
                    
                    
            print('Running PDFtex')
            
            # Change directory, run latex, delete files
            os.chdir(dirpath)    
            args = ['pdflatex',
                    '-synctex=1',
                    '-interaction=nonstopmode',
                    filename]
            
            # Bruk pdflatex på filen
            subprocess.check_call(args, cwd=dirpath, stdout=subprocess.DEVNULL)
            print('{} -> {}'.format(filename, filename.replace('.tex', '.pdf')))
 
    