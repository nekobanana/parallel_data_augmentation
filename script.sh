#!/bin/bash
python=".venv/bin/python"
base_dir="/media/quacksort/OS/Users/giorg/parallel"
#$python sequential.py -i input_images_resized -o "$base_dir/output_images_resized" -a 40 -r "results_resized/seq.txt"
for p in 22 24 26 28 30
#for p in 2 4 6 8 10 12 14 16 18 20
do
  $python parallel_transf.py -i input_images_resized -o "$base_dir/output_images" -a 40 -p "$p" -r "results_resized/parallel_trans_$p.txt"
  $python parallel_images.py -i input_images_resized -o "$base_dir/output_images" -a 40 -p "$p" -r "results_resized/parallel_images_$p.txt"
done
