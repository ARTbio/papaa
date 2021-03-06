#!/usr/bin/env python3

"""
Flatten out a within_disease classifier directory
"""

import os
import sys
import argparse
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'papaa'))
from tcga_util import add_version_argument

parser = argparse.ArgumentParser()
add_version_argument(parser)
parser.add_argument('-i', '--input-directory', default=None,
                    help='Input Classifier directory')
parser.add_argument('-o', '--output-directory', default=None,
                    help='Directory to put flattened collection')

args = parser.parse_args()

root_out_path = os.path.join(args.output_directory, 'root')
os.makedirs(root_out_path, exist_ok=True)
within_disease_out_path = os.path.join(args.output_directory, 'within_disease')
os.makedirs(within_disease_out_path, exist_ok=True)
disease_out_path = os.path.join(args.output_directory, 'disease')
os.makedirs(disease_out_path, exist_ok=True)
for path in os.listdir(os.path.join(args.input_directory)):
    if os.path.isfile(os.path.join(args.input_directory, path)):
        # These should not exist
        #shutil.move(os.path.join(args.input_directory, 'within_disease', path), os.path.join(root_out_path, os.path.basename(path)))
        continue
    else:
        disease = path
        for path in os.listdir(os.path.join(args.input_directory, disease)):
            if os.path.isfile(os.path.join(args.input_directory, disease, path)):
                shutil.move(os.path.join(args.input_directory, disease, path), os.path.join(within_disease_out_path, '%s_%s' % (disease, os.path.basename(path))))
            else:
                assert path == 'disease', ValueError("Unexpected directory: %s" % path)
                for subpath in os.listdir(os.path.join(args.input_directory, disease, path)):
                    shutil.move(os.path.join(args.input_directory, disease, path, subpath), os.path.join(disease_out_path, os.path.basename(subpath)))
