#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mkdir -p data
mv Pokemon.csv data
head -4 data/Pokemon.csv > data/Pokemon.small.csv

echo "download completed!"
