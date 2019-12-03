#!/bin/bash
mkdir -p app/data
gzip --keep sample.json
mv sample.json.gz app/data
