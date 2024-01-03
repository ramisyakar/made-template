#!/bin/bash

pip install --upgrade pip
pip install -r ./project/requirements.txt

python -m unittest project/test_pipeline.py