#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

mv Pokemon.csv data

echo "download completed!"
