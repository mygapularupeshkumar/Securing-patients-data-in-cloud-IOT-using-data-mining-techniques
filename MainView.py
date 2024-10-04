"""
=============================================================================================================================================================================================
==                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ==
==                                                                                                                                       TITLE: - SECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES                                                                                                                                                               ==
==                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ==
=============================================================================================================================================================================================

"""
import time
from customtkinter import CTkButton as Button
from tkinter import Label, Tk
from tkinter import messagebox
from plyer import notification
from LoadCSV import *
from Metrics import PerformanceMetrics
from Preprocess import *
from Leach import *
from HLT import *
from GAN import *
from Feature import *
from Monitoring import *
import warnings
import logging
logging.getLogger().setLevel(logging.ERROR)
warnings.filterwarnings("ignore")
def Start():
    print("=============================================================================")
    print("\n\tSECURING PATIENT DATA IN CLOUD IOT USING DATA MINING TECHNIQUES\n")
    print("=============================================================================")
    time.sleep(2)
    print ("\n==========================************* LOADING THE DATASET ********======================")    
    time.sleep(2)
    load_data()
    time.sleep(2)
    messagebox.showinfo("Message", "Collecting and Loading the Cleveland Heart Disease Dataset Completed")
    print("\n========================================================================================\n")

def PreProcessing():
    print ("\n==========================************* SMOTE ALGORITHM BASED DATA PRE-PROCESSING PROCESS ********======================")    
    time.sleep(2)
    SMOTE_Algorithm()
    time.sleep(2)
    messagebox.showinfo("Message", "Data Pre-Processing using SMOTE Completed")
    print("\n========================================================================================\n")

def Feature_Extraction():
    print ("\n==========================************* PCA ALGORITHM BASED FEATURE EXTRACTION PROCESS ********======================\n")       
    time.sleep(2)
    PCA_Algorithm()
    time.sleep(2)
    messagebox.showinfo("Message", "Feature Extraction using PCA Completed")
    print("\n========================================================================================\n")

def Classification():
    print ("\n==========================*************   GAN WITH ADAM ALGORITHM BASED CLASSIFICATION PROCESS  ********======================")
    time.sleep(2)
    GAN_Classification()
    time.sleep(2)
    messagebox.showinfo("Message", "Classification using GAN with ADAM Completed")
    print("\n========================================================================================\n")

def Data_Transmission():
    print ("\n==========================******************* DATA TRANSMISSION PROCESS *******************==========================")
    time.sleep(2)
    print("\nHLT Encryption and Decryption is Under Process......")
    time.sleep(2)
    HLT_Algorithm()
    time.sleep(2)
    messagebox.showinfo("Message", "HLT Encryption and Decryption Completed")
    print("\n========================================================================================\n")
    time.sleep(2)
    print("\nLEACH Protocol Routing is Under Process......")
    time.sleep(2)
    Leach_Transmission()
    time.sleep(2)
    messagebox.showinfo("Message", "Routing of Data using Leach Protocol Completed")
    print("\n========================================================================================\n")
    time.sleep(2)
    print("\nData Storing is Under Process......")
    time.sleep(2)
    Storage()
    time.sleep(2)
    messagebox.showinfo("Message", "Data Storing Process Completed")
    print("\n========================================================================================\n")

def Monitor():
    print ("\n==========================*************   MONITORING OF CLOUD DATA  PROCESS ********======================")
    time.sleep(2)
    IoT_Monitor()
    time.sleep(2)
    messagebox.showinfo("Message", "Monitoring of Cloud Data Completed")
    print("\n========================================================================================\n")

def Performance_Metrics():
    print ("\n==========================******************* PERFORMANCE METRICS *******************==========================")
    time.sleep(2)
    PerformanceMetrics()
    time.sleep(2)
    messagebox.showinfo("Message", "Performance Metrics Completed")
    print("\n========================================================================================\n")
    time.sleep(3)
    window.destroy()

def main():
    global window
    window = Tk()
    window.title("Securing Patient Data in Cloud Iot")
    window_width = 850
    window_height = 680
    window.geometry(f"{window_width}x{window_height}")
    window.resizable(False, False)
    window.configure(background="#505050")
    button_params = {'width':285, 'height':55, 'fg_color':'#df3939', 'text_color':'#ffffff','corner_radius':50, 'font': ('Georgia', 14,'bold')}
    label_params = {'bg':'#20b61b', 'fg':'#000000', 'width':500, 'height':4, 'font':('Georgia', 18)}
    Label(window, text="SECURING PATIENT DATA IN CLOUD IOT\nUSING DATA MINING TECHNIQUES",**label_params).pack()
    Label(window, text=" ",bg='#505050').pack()
    b1 = Button(window,text="START", **button_params, command=Start)
    b1.pack(pady=10)
    b2 = Button(window,text="PRE-PROCESSING", **button_params, command=PreProcessing)
    b2.pack(pady=10)
    b3 = Button(window,text="FEATURE EXTRACTION", **button_params, command=Feature_Extraction)
    b3.pack(pady=10)
    b3 = Button(window,text="CLASSIFICATION", **button_params, command=Classification)
    b3.pack(pady=10)
    b4 = Button(window,text="DATA TRANSMISSION", **button_params, command=Data_Transmission)
    b4.pack(pady=10)
    b5 = Button(window,text="MONITOR", **button_params, command=Monitor)
    b5.pack(pady=10)
    b6 = Button(window, text="PERFORMANCE METRICS", **button_params, command=Performance_Metrics)
    b6.pack(pady=10)
    window.mainloop()

if __name__ == "__main__":
    main()

