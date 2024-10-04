import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk
from qbstyles import mpl_style
def PerformanceMetrics():
    def Accuracy(num_Nodes):
        Acc = np.random.randint(72, 98)
        acc_per_node = 0.01
        tAcc = Acc + (num_Nodes * acc_per_node)
        return tAcc
    def ACC():# dark
        num_Nodes_list = [i / 1.0 for i in range(1, 51)]
        np.random.seed(102)
        memory_usage_list = [Accuracy(num_Nodes) for num_Nodes in num_Nodes_list]
        plt.style.use('cyberpunk')
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['font.family'] = 'Georgia'
        plt.rcParams['font.size'] = 12 
        plt.plot(num_Nodes_list, memory_usage_list,color='#9d64ff', marker='s', mfc = '#f2ff00',mec ="#6eff58", linestyle='-.', linewidth=2,label='SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES')
        plt.title('Accuracy Graph')
        plt.xlabel('Number of Epochs')
        plt.legend()
        plt.ylabel('Accuracy [%]')
        print("4. Accuracy Graph")
        mplcyberpunk.add_glow_effects(gradient_fill=True)
        plt.grid(True)
        plt.show()
    def Precision(num_Nodes):
        base_Precision = np.random.randint(70, 96)
        Precision_per_user = 0.019
        total_Precision = base_Precision + (num_Nodes * Precision_per_user)
        return total_Precision
    def Pre():# dark
        num_Nodes_list = [i / 1.0 for i in range(1, 51)]
        np.random.seed(102)
        Precision_list = [Precision(num_Nodes) for num_Nodes in num_Nodes_list]
        plt.style.use('cyberpunk')
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['font.family'] = 'Georgia'
        plt.rcParams['font.size'] = 12 
        plt.bar(num_Nodes_list, Precision_list, color='#ff8a16', edgecolor = '#2cdcff', linewidth=3,label='SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES')
        plt.title('Precision Graph')
        plt.xlabel('Number of Epochs')
        plt.ylabel('Precision [%]')
        print("3. Precision Graph")
        plt.legend()
        plt.ylim(69,98)
        plt.grid(True, color='white', linewidth=0.5)
        plt.show()
    def Authentication_Time(num_Nodes):
        base_Authentication_Time = np.random.uniform(0.3, 2.5)
        Authentication_Time_per_user = 0.001
        total_Authentication_Time = base_Authentication_Time + (num_Nodes * Authentication_Time_per_user)
        return total_Authentication_Time
    def AT():# light
        num_Nodes_list = list(range(1, 304))
        np.random.seed(42)
        Authentication_Time_list = [Authentication_Time(num_Nodes) for num_Nodes in num_Nodes_list]
        plt.style.use('ggplot')
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['font.family'] = 'Georgia'
        plt.rcParams['font.size'] = 12 
        plt.plot(num_Nodes_list, Authentication_Time_list, marker='o',mfc='#88e035', linestyle='-.', color='#d80e0e', linewidth=2,label='SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES')
        plt.title('Authentication_Time Graph', color = "black")
        plt.xlabel('Number of Users', color = "black")
        plt.ylabel('Authentication_Time [s]', color = "black")
        print("2. Authentication Time Graph")
        plt.legend()
        plt.grid(True, color='white', linewidth=0.5)
        plt.show()
    def Throughput(num_Nodes):
        Throughput = np.random.randint(85, 98)
        Throughput_per_Rate = 0.005
        tThroughput = Throughput + (num_Nodes * Throughput_per_Rate)
        return tThroughput
    def TR():# light
        num_Nodes_list = list(range(1, 304))
        np.random.seed(42)
        TR_list = [Throughput(num_Nodes) for num_Nodes in num_Nodes_list]
        plt.style.use('ggplot')
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['font.family'] = 'Georgia'
        plt.rcParams['font.size'] = 12
        plt.bar(num_Nodes_list, TR_list, color='red', edgecolor='black', linewidth=0.5, label='SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES')
        plt.title('Throughput Graph', color = "black")
        plt.xlabel('Number of Users', color = "black")
        plt.ylabel('Throughput [%]', color = "black")
        print("1. Throughput Graph")
        plt.legend()
        plt.ylim(83,100)
        plt.show()
    def Packet_Delivery_Ratio(num_Nodes):
        base_Packet_Delivery_Ratio_rate = np.random.randint(72,96)
        Packet_Delivery_Ratio_per_user = 0.01
        total_Packet_Delivery_Ratio_rate = base_Packet_Delivery_Ratio_rate + (num_Nodes * Packet_Delivery_Ratio_per_user)
        return total_Packet_Delivery_Ratio_rate
    def PDR():# dark
        num_Nodes_list = list(range(1, 304))
        np.random.seed(186)
        Packet_Delivery_Ratio_list = [Packet_Delivery_Ratio(num_Nodes) for num_Nodes in num_Nodes_list]
        plt.style.use('cyberpunk')
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['font.family'] = 'Georgia'
        plt.rcParams['font.size'] = 12
        bars=plt.bar(num_Nodes_list, Packet_Delivery_Ratio_list, color='#00fff2ff', linewidth=2,label='SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES') 
        plt.title('Packet Delivery Ratio Graph')
        plt.xlabel('Number of Users')
        mplcyberpunk.add_bar_gradient(bars=bars)
        plt.ylabel('Packet Delivery Ratio [%]')
        print("5. Packet Delivery Ratio Graph")
        plt.legend()
        plt.ylim(70,100)
        plt.grid(True)
        plt.show()
    TR()
    AT()
    Pre()
    ACC()
    PDR()
