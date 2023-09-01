#!/usr/bin/env bash


dataset="ENZYMES"
output_dir="../results/tu/"$dataset"/"

mkdir -p $output_dir"board/"
mkdir -p $output_dir"error/"
mkdir -p $output_dir"stdout/"

config_file="./configs/"$dataset".json"


#source ../.venv/bin/activate
#python -u ./generate-tu-matrices.py --config=$config_file 
#deactivate


eval "$(conda shell.bash hook)"
conda activate sage310
python ./generate-tu-skewS.py --config=$config_file
conda deactivate

echo "Finished generation"
