#!/bin/bash
python=".venv/bin/python"
base_dir="/media/quacksort/OS/Users/giorg/parallel"
for p in 2 4 6 8 12 16 20 24 28 32
do
  $python parallel_transf.py -i input_images -o "$base_dir/output_images" -a 40 -p "$p" -r "results/parallel_trans_$p.txt"
  $python parallel_images.py -i input_images -o "$base_dir/output_images" -a 40 -p "$p" -r "results/parallel_images_$p.txt"
done
$python sequential.py -i input_images -o "$base_dir/output_images" -a 40 -r "results/seq.txt"