#!/bin/bash
kaggle datasets download -d abcsds/pokemon
unzip pokemon.zip
rm pokemon.zip

echo "download completed!"
