import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
def Leach_Transmission():
    def leach_clustering(nodes, threshold):
        clusters = []
        for node in nodes:
            if np.random.uniform(0, 1) < threshold:
                cluster = {'head': node, 'members': [node]}
                clusters.append(cluster)
        return clusters
    def simulate_transmission(Patients, cloud_nodes, energy_data, communication_data):
        energy_consumption = 0
        communication_rate = 0
        for iot_node in Patients:
            for cloud_node in cloud_nodes:
                idx = np.random.randint(len(energy_data))
                energy_consumption += energy_data[idx]  
                communication_rate += communication_data[idx]  
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                plt.plot([iot_node['x'], cloud_node['x']], [iot_node['y'], cloud_node['y']], c=color, linestyle='--', alpha=0.5)
        return energy_consumption, communication_rate
    dataset = pd.read_csv("Output/decrypted_dataset.csv")
    energy_consumption_data = dataset['thalach'].values  
    communication_rate_data = dataset['slope'].values    
    num_Patients = 300
    num_cloud_nodes = 5
    grid_size = 100  
    initial_energy = 100 
    initial_cloud_energy = 10000  
    rounds = 20  
    threshold = 0.1  
    Patients = [{'x': np.random.randint(0, grid_size),
                'y': np.random.randint(0, grid_size),
                'energy': initial_energy} for _ in range(num_Patients)]
    cloud_positions = [(110, 20),  
                    (-10, 20),  
                    (110, 80),  
                    (-10, 80),  
                    (50, 110)] 
    cloud_nodes = [{'x': pos[0], 'y': pos[1], 'energy': initial_cloud_energy} for pos in cloud_positions]
    fig, ax = plt.subplots()
    ax.scatter([node['x'] for node in Patients], [node['y'] for node in Patients], c='blue', marker='o',s=50,label = 'IoT Nodes')
    ax.scatter([node['x'] for node in cloud_nodes], [node['y'] for node in cloud_nodes], c='red', marker='^', s=300, alpha=0.5,label = 'Cloud')  
    ax.set_xlim(-20, grid_size*1.2)  
    ax.set_ylim(0, grid_size*1.2)
    ax.set_title('Data Transmission Using Leach Protocol from IoT Nodes to Cloud Nodes')
    for round_num in range(rounds):
        iot_clusters = leach_clustering(Patients, threshold)
        energy_consumption, communication_rate = simulate_transmission(Patients, cloud_nodes, energy_consumption_data, communication_rate_data)
        print("Round {}: Energy Consumption per Joule - {:.2f} J, Communication Rate - {:.2f} Mbps".format(round_num+1, energy_consumption, communication_rate))
        plt.pause(1)  
    plt.legend()
    plt.show()
def Storage():
    dataset = pd.read_csv("Output/decrypted_dataset.csv")
    server_path = 'Cloud_Server'
    if not os.path.exists(server_path):
        os.makedirs(server_path)
    server_filename = 'Patient_HealthCare_Data.csv'
    server_file_path = os.path.join(server_path, server_filename)
    dataset.to_csv(server_file_path, index=False)
    print(f"Data stored successfully in '{server_file_path}' on the Cloud Architecture server.")
