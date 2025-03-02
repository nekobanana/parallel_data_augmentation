#!/bin/bash
python=".venv/bin/python"
base_dir="/media/quacksort/OS/Users/giorg/parallel"
for p in 4 8 16 32;
do
  $python parallel_transf.py -i input_images -o "$base_dir/output_images" -a 50 -p "$p" -r "results/parallel_trans_async_$p.txt"
  $python parallel_images.py -i input_images -o "$base_dir/output_images" -a 50 -p "$p" -r "results/parallel_images_async_$p.txt"
done
#$python sequential.py -i input_images -o "$base_dir/output_images" -a 50 -r "results/seq.txt"