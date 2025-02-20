#!/bin/bash
python=".venv/bin/python"
for p in $(seq 4 4 32);
do
  $python parallel_transf.py -i input_images -o output_images -a 100 -p "$p" -r "results/parallel_trans_{$p}.txt"
  $python parallel_images.py -i input_images -o output_images -a 100 -p "$p" -r "results/parallel_images_{$p}.txt"
done
$python sequential.py -i input_images -o output_images -a 100 -r "results/parallel_images_{$p}.txt"