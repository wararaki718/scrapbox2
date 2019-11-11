#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mkdir -p sample_pipeline_app/data
mv Pokemon.csv sample_pipeline_app/data

echo "download completed!"
