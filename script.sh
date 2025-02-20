#!/bin/bash
python=".venv/bin/python"
base_dir="/media/quacksort/OS/Users/giorg/parallel"
for p in $(seq 8 8 32);
do
  $python parallel_transf.py -i input_images -o "$base_dir/output_images" -a 10 -p "$p" -r "results/parallel_trans_$p.txt"
  $python parallel_images.py -i input_images -o "$base_dir/output_images" -a 10 -p "$p" -r "results/parallel_images_$p.txt"
done
$python sequential.py -i input_images -o "$base_dir/output_images" -a 10 -r "results/parallel_images_$p.txt"