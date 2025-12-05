#!/bin/bash

# Chemin vers Python (optionnel si python est dans ton PATH)
PYTHON=python

# Arguments par défaut
AUDIO_DEVICE_INDEX=1
ACCESS_KEY="NKRtiAYvAOx1FaZSg24Bvs5ZvPGQqySE4fKPWEH6rHV3WQZGnzucgw=="
MODEL_PATH="models/porcupine_params_fr.pv"
KEYWORD_PATHS="keyword_files/linux/c3p0_linux_v3.ppn"
LANG="fr"

$PYTHON main.py \
  --audio_device_index $AUDIO_DEVICE_INDEX \
  --access_key $ACCESS_KEY \
  --model_path $MODEL_PATH \
  --keyword_paths $KEYWORD_PATHS \
  -m $LANG