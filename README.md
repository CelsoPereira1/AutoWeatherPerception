# Weather and Meteorological Optical Range Classification for Autonomous Driving

Companion code to the submission:
"Weather and Meteorological Optical Range Classification for Autonomous Driving" by Celso Pereira, João N. D. Fernandes, Ricardo P. M. Cruz, João Ribeiro Pinto, Jaime S. Cardoso. IEEE Transactions on Intelligent Vehicles.

## Abstract: 

Weather and meteorological optical range (MOR) perception is crucial for smooth and safe autonomous driving (AD). This article introduces two deep learning-based architectures designed for concurrent weather and MOR classification in AD, employing multi-modal, multi-task approaches. Extensive experiments employing the publicly available FogChamber dataset, demonstrate that the first architecture, characterized by its lightweight design and simplicity, achieves an accuracy of 98.88% in weather classification and 89.77% in MOR classification, with a modest memory allocation of 5.33 megabytes (MB) and an inference time of 2.50 milliseconds (ms). The second architecture prioritizes performance, achieving higher accuracies of 99.38% in weather classification and 91.88% in MOR classification. However, it requires a more substantial memory allocation of 54.06 MB and exhibits a longer inference time of 15.55 ms. Compared to other state-of-the-art architectures, the proposed methods show an important trade-off between accuracy performance, inference time, and memory allocation, which are crucial parameters for enabling autonomous driving.

## Proposed Architectures and Baseline

### Multi-task architecture featuring the MobileNetV3-Small encoder and early fusion:

![MobileNetV3 Architecture](https://github.com/CelsoPereira1/AutoWeatherPerception/files/13938981/MobileNetV3.pdf)

### Multi-task architecture featuring the MobileNetV3-Small encoder and cross-modal self-attention intermediate fusion:

![MobileNetV3ViT Architecture](https://github.com/CelsoPereira1/AutoWeatherPerception/files/13938983/MobileNetV3ViT.pdf)

### Baseline architecture featuring the TransFuser encoder and cross-modal self-attention intermediate fusion:

![ResNetViT Architecture](https://github.com/CelsoPereira1/AutoWeatherPerception/files/13938988/ResNetViT.pdf)

## Code:

The provided Bash script, "W_MOR_Classification_MM_MT&ST.sh," enables the simultaneous execution of code for both multi-task (MT) and single-task (ST) approaches. Users can vary the following options within the script:

- `NETWORKS`: Choose from "MobileNetV3_Early," "MobileNetV3_ViT," and "ResNet_ViT" (Baseline).

- `OPT_TECHNIQUES`: Select between "Multi_Adaptive" and "Weighted."

- `TRAIN_MODEL`: Set to either "True" or "False" based on whether the model should be trained or not.

Other fixed parameters include:

- `EPOCHS`: Set, for example, to 50.

- `BATCH`: Set, for example, to 16.

- `SEED`: Set, for example, to 10.

Users can tailor the script by modifying these parameters to experiment with the different network architectures, optimization techniques, and training configurations.

Following the training, validation, and testing phases of the models, their performance can be automatically presented using the provided code in "W_MOR_Classification_MM_MT&ST_Performance.py".

**Contact:** Celso Pereira, up202200546@up.pt
