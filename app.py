import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

data_set = pd.read_csv("feature_trained.csv")
st.header("IoT Device Type Identification Using Supervised Machine Learning")
st.subheader("This section will help you determine the type of IoT Device you have (Baby Monitor, Lights, Motion Sensor, Security Camera, Smoke Detector, Socket, Thermostat, TV, Watch and Water Sensor)")
st.text("Kindly fill out all the input fields in order to see the results.")

st.dataframe(data_set)
http_time_avg = st.number_input("HTTP Time Average")
ttl_avg = st.number_input("TTL Average")
packet_inter_arrivel_B_firstQ = st.number_input("Packet Arrival Time B First")
packet_inter_arrivel_A_sum = st.number_input("Summation of Packet Arrival Time A")
packet_inter_arrivel_B_min = st.number_input("Minimum Packet Arrival Time B")

features = ['http_time_avg', 'ttl_avg', 'packet_inter_arrivel_B_firstQ', 'packet_inter_arrivel_A_sum',
            'packet_inter_arrivel_B_min']
X = data_set[features]
y = data_set['device_category']
X = np.nan_to_num(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
clf = XGBClassifier(n_estimators=100)
clf.fit(X_train, y_train)
predict_val = clf.predict([[http_time_avg, ttl_avg, packet_inter_arrivel_B_firstQ, packet_inter_arrivel_A_sum, packet_inter_arrivel_B_min]])
predict_val = float(predict_val)

if predict_val == 1:
    st.info("Device Category: Lights")

elif predict_val == 2:
    st.info("Device Category: Motion Sensor")

elif predict_val == 3:
    st.info("Device Category: Security Camera")

elif predict_val == 4:
    st.info("Device Category: Smoke Detector")

elif predict_val == 5:
    st.info("Device Category: Socket")

elif predict_val == 6:
    st.info("Device Category: Thermostat")

elif predict_val == 7:
    st.info("Device Category: Television")

elif predict_val == 8:
    st.info("Device Category: Watch")

elif predict_val == 9:
    st.info("Device Category: Water Sensor")

else:
    st.info("Device Category: Baby Monitor")