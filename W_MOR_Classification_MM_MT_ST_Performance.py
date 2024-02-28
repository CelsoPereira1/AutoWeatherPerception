import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_metrics_file(file_path):
    data = pd.read_csv(file_path)
    return data

def process_metrics_files(networks, opt_techniques, seeds, folder_path="./"):
    grouped_files = {}

    for network in networks:
        for opt_technique in opt_techniques:
            for seed in seeds:
                for file in os.listdir(folder_path):
                    if file.startswith(f'MT_MM_W_MOR_Class_Metrics_Network_{network}_Optimization_{opt_technique}_Seed_{seed}')and file.endswith('.csv'):
                        common_name = '_'.join(file.split('_')[:-2])  # Extract common name excluding the seed
                        if common_name not in grouped_files:
                            grouped_files[common_name] = []
                        grouped_files[common_name].append(read_metrics_file(os.path.join(folder_path, file)))

    for network in networks:
        for seed in seeds:
            for file in os.listdir(folder_path):
                if file.startswith(f'ST_MM_W_MOR_Class_Metrics_Network_{network}_Seed_{seed}') and file.endswith('.csv'):
                    common_name = '_'.join(file.split('_')[:-2])
                    if common_name not in grouped_files:
                        grouped_files[common_name] = []
                    grouped_files[common_name].append(read_metrics_file(os.path.join(folder_path, file)))

    return grouped_files

if __name__ == "__main__":
    NETWORKS = ["RangeWeatherNet_Early", "MobileWeatherNet_Early"] # "MobileNetV3_Early", "MobileNetV3_ViT", "ResNet_ViT"
    OPT_TECHNIQUES = ["Multi_Adaptive", "Weighted"]
    SEEDS = [10, 21, 29, 38, 64, 65, 70, 72, 81, 89]

    all_data_dict = process_metrics_files(NETWORKS, OPT_TECHNIQUES, SEEDS)

    for key, value in all_data_dict.items():
        weather_accuracy_values = []
        weather_cohenkappa_values = []
        weather_f1_values = []
        visibility_accuracy_values = []
        visibility_cohenkappa_values = []
        visibility_f1_values = []
        memory_values = []
        mean_inference_time_values = []

        for i in range(len(value)):
            weather_accuracy = value[i].at[0, 'Value']*100
            weather_cohenkappa = value[i].at[1, 'Value']*100
            weather_f1 = value[i].at[2, 'Value']*100
            visibility_accuracy = value[i].at[3, 'Value']*100
            visibility_cohenkappa = value[i].at[4, 'Value']*100
            visibility_f1 = value[i].at[5, 'Value']*100
            memory = value[i].at[6, 'Value']
            mean_inference_time = value[i].at[7, 'Value']

            weather_accuracy_values.append(weather_accuracy)
            weather_cohenkappa_values.append(weather_cohenkappa)
            weather_f1_values.append(weather_f1)
            visibility_accuracy_values.append(visibility_accuracy)
            visibility_cohenkappa_values.append(visibility_cohenkappa)
            visibility_f1_values.append(visibility_f1)
            memory_values.append(memory)
            mean_inference_time_values.append(mean_inference_time)

        # calculate mean and std for each variable
        weather_accuracy_mean = np.mean(weather_accuracy_values)
        weather_accuracy_std = np.std(weather_accuracy_values)

        weather_cohenkappa_mean = np.mean(weather_cohenkappa_values)
        weather_cohenkappa_std = np.std(weather_cohenkappa_values)

        weather_f1_mean = np.mean(weather_f1_values)
        weather_f1_std = np.std(weather_f1_values)

        visibility_accuracy_mean = np.mean(visibility_accuracy_values)
        visibility_accuracy_std = np.std(visibility_accuracy_values)

        visibility_cohenkappa_mean = np.mean(visibility_cohenkappa_values)
        visibility_cohenkappa_std = np.std(visibility_cohenkappa_values)

        visibility_f1_mean = np.mean(visibility_f1_values)
        visibility_f1_std = np.std(visibility_f1_values)

        memory_mean = np.mean(memory_values)
        memory_std = np.std(memory_values)

        mean_inference_time_mean = np.mean(mean_inference_time_values)
        mean_inference_time_std = np.std(mean_inference_time_values)

        print(f"Key: {key}")
        print(f"Weather Accuracy: Mean={weather_accuracy_mean:.2f}, Std={weather_accuracy_std:.2f}")
        print(f"Weather Cohen Kappa: Mean={weather_cohenkappa_mean:.2f}, Std={weather_cohenkappa_std:.2f}")
        print(f"Weather F1: Mean={weather_f1_mean:.2f}, Std={weather_f1_std:.2f}")
        print(f"Visibility Accuracy: Mean={visibility_accuracy_mean:.2f}, Std={visibility_accuracy_std:.2f}")
        print(f"Visibility Cohen Kappa: Mean={visibility_cohenkappa_mean:.2f}, Std={visibility_cohenkappa_std:.2f}")
        print(f"Visibility F1: Mean={visibility_f1_mean:.2f}, Std={visibility_f1_std:.2f}")
        print(f"Memory: Mean={memory_mean:.2f}, Std={memory_std:.2f}")
        print(f"Mean Inference Time: Mean={mean_inference_time_mean:.2f}, Std={mean_inference_time_std:.2f}")
        print("\n")

        data = [weather_accuracy_values, weather_cohenkappa_values, weather_f1_values, visibility_accuracy_values, visibility_cohenkappa_values, visibility_f1_values]
        labels = ['W_Acc', 'W_κ', 'W_F1', 'MOR_Acc', 'MOR_κ', 'MOR_F1']

        sns.set_style(style='whitegrid')
        sns.set(font_scale=1.2, rc={'font.family': 'serif'})
        plt.figure(figsize=(10, 6))
        ax = sns.violinplot(data=data, inner="quartile", color='gray')
        ax.set(xticklabels=labels, ylabel='Value', title=f'Performance')
        ax.grid(True, linestyle='--', alpha=0.7)
        sns.despine() # remove top and right spines
        plt.savefig(f"Violin_Plot_{key}.pdf")
        plt.close()