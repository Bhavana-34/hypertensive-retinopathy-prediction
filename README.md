RetinoScan
Deep Learning for Medical Diagnosis from Retinal Images
June 2024 – May 2025

Overview
RetinoScan is a cutting-edge deep learning pipeline designed to diagnose multiple diseases—Diabetes, Hypertension, and Autism—using retinal images. It leverages convolutional neural networks (CNN), advanced image preprocessing, segmentation, and real-time visualization via a user-friendly Streamlit dashboard to support early detection and diagnosis.

Key Features
Robust Disease Classification: Achieved 79% AUC score with a custom-trained CNN trained on over 1,400 labeled retinal images.

Image Enhancement: Implemented multiple preprocessing techniques and data augmentation, boosting image clarity by 25%.

Segmentation & Feature Extraction: Performed optic disc segmentation on over 5,000 retinal images, significantly improving model accuracy.

Interactive Dashboard: An intuitive Streamlit app visualizes real-time disease severity scores, helping clinicians monitor diagnosis bottlenecks efficiently.

Technologies & Libraries
Python for core development

TensorFlow and Keras for deep learning models

OpenCV for image processing and segmentation

Streamlit for creating interactive dashboards

Getting Started
Clone the Repository
bash
git clone https://github.com/Bhavana-34/microburnoutthis.git
Install Dependencies
Create and activate a virtual environment, then install required packages:

bash
pip install -r requirements.txt
Prepare Data & Train Model
Run preprocessing scripts on your retinal dataset

Use the training notebooks provided for CNN architecture tuning

Track the training progress and validation performance

Launch the Dashboard
bash
streamlit run app.py
Open your browser, navigate to the local URL, and start diagnosing!

Future Work & Enhancements
Extending disease detection capabilities to additional conditions

Improving model accuracy with larger datasets and advanced architectures

Deploying the app for mobile or cloud-based access

Integrating more seamless data input options

Acknowledgments
Special thanks to all dataset providers and contributors. Your support makes this project possible.

License
This project is licensed under the MIT License — see the LICENSE file for details.

Contact
For questions or collaborations, please reach out to Bhavana Koli at bhavanakoli2022@vitbhopal.ac.in.

