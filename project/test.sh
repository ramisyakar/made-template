#!/bin/bash

pip install --upgrade pip
pip install -r ./project/requirements.txt

pytest ./project/test_pipeline.py