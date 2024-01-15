#!/bin/bash
NETWORKS="MobileNetV3_ViT ResNet_ViT MobileNetV3_Early"
OPT_TECHNIQUES="Multi_Adaptive Weighted"
TRAIN_MODEL="True"
EPOCHS=50
BATCH=16
SEED=10

for NETWORK in $NETWORKS; do
    for OPT_TECHNIQUE in $OPT_TECHNIQUES; do
        echo "python3 ./W_MOR_Classification_MM_MT.py $BATCH $EPOCHS $NETWORK $OPT_TECHNIQUE $TRAIN_MODEL $SEED"
        python3 ./W_MOR_Classification_MM_MT.py $BATCH $EPOCHS $NETWORK $OPT_TECHNIQUE $TRAIN_MODEL $SEED
    done
    echo "python3 ./W_MOR_Classification_MM_ST.py $BATCH $EPOCHS $NETWORK $TRAIN_MODEL $SEED"
    python3 ./W_MOR_Classification_MM_ST.py $BATCH $EPOCHS $NETWORK $TRAIN_MODEL $SEED
done