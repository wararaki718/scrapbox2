#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mkdir -p app/data
mv Pokemon.csv app/data

echo "download completed!"
