#!/bin/bash
NETWORKS="RangeWeatherNet_Early MobileWeatherNet_Early"
OPT_TECHNIQUES="Multi_Adaptive Weighted"
TRAIN_MODEL="True"
EPOCHS=50
BATCH=16
SEEDS=(10 21 29 38 64 65 70 72 81 89) # SEEDS=($(shuf -i 1-100 -n 10))

for SEED in "${SEEDS[@]}"; do
    for NETWORK in $NETWORKS; do
        for OPT_TECHNIQUE in $OPT_TECHNIQUES; do
            echo "python3 ./W_MOR_Classification_MM_MT.py $BATCH $EPOCHS $NETWORK $OPT_TECHNIQUE $TRAIN_MODEL $SEED"
            # python3 ./W_MOR_Classification_MM_MT.py $BATCH $EPOCHS $NETWORK $OPT_TECHNIQUE $TRAIN_MODEL $SEED
            sbatch python3 ./W_MOR_Classification_MM_MT.py $BATCH $EPOCHS $NETWORK $OPT_TECHNIQUE $TRAIN_MODEL $SEED
        done
        echo "python3 ./W_MOR_Classification_MM_ST.py $BATCH $EPOCHS $NETWORK $TRAIN_MODEL $SEED"
        # python3 ./W_MOR_Classification_MM_ST.py $BATCH $EPOCHS $NETWORK $TRAIN_MODEL $SEED
        sbatch python3 ./W_MOR_Classification_MM_ST.py $BATCH $EPOCHS $NETWORK $TRAIN_MODEL $SEED
    done
done