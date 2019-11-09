#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mkdir -p sample_ml_app/data
mv Pokemon.csv sample_ml_app/data

echo "download completed!"
