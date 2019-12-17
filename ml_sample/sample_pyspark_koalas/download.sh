#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mkdir -p data
mv Pokemon.csv data

echo "download completed!"
