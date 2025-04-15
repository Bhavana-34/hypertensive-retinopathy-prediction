{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c4e804f-bc52-410a-ac9b-a759de79ec92",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-16 01:14:23.411 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.412 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.413 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.414 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.416 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.418 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.420 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.420 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.422 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.423 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.424 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.427 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.428 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-16 01:14:23.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the pre-trained model (slope and intercept)\n",
    "with open(\"slope.pkl\", \"rb\") as f:\n",
    "    m = pickle.load(f)\n",
    "\n",
    "with open(\"intercept.pkl\", \"rb\") as f:\n",
    "    c = pickle.load(f)\n",
    "\n",
    "# Function to classify the point\n",
    "def point_position_parallel(m, c, point):\n",
    "    x, y = point\n",
    "    y_on_line = m * x + c\n",
    "\n",
    "    if y > y_on_line:\n",
    "        return \"No Hypertensive Retinopathy\"\n",
    "    elif y < y_on_line:\n",
    "        return \"Hypertensive Retinopathy\"\n",
    "    else:\n",
    "        return \"Borderline/Unclear\"\n",
    "\n",
    "# Streamlit UI elements\n",
    "st.title(\"Hypertensive Retinopathy Prediction\")\n",
    "\n",
    "st.write(\"\"\"\n",
    "    This tool classifies whether a point (disc diameter vs. cup diameter)\n",
    "    indicates the presence of **Hypertensive Retinopathy** based on the fitted model.\n",
    "\"\"\")\n",
    "\n",
    "# User input\n",
    "disc_diameter = st.number_input(\"Enter Disc Diameter:\", min_value=0.0, step=0.01)\n",
    "cup_diameter = st.number_input(\"Enter Cup Diameter:\", min_value=0.0, step=0.01)\n",
    "\n",
    "# When the user clicks the \"Predict\" button\n",
    "if st.button(\"Predict\"):\n",
    "    if disc_diameter > 0 and cup_diameter > 0:\n",
    "        result = point_position_parallel(m, c, (disc_diameter, cup_diameter))\n",
    "        st.write(f\"Prediction: {result}\")\n",
    "    else:\n",
    "        st.write(\"Please enter valid values for both Disc Diameter and Cup Diameter.\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17e9c394-97dc-4e2d-b19a-4c7f4ab1d4fe",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6a13045-a7f8-4814-8dbd-8370d21b33ee",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
