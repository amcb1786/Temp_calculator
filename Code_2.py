#!/usr/bin/env python
# coding: utf-8

# In[1]:


# input tempreature 
temperature = input("Enter the patient's temperature in degrees Fahrenheit: ")


# In[2]:


# check tempreature
if temperature.replace(".", "",1).isdigit(): 
    temperature_input = float(temperature)
    if temperature_input >= 99.5:
        print("The patient has a high temperature.")
    else: 
        print("The patient has a normal temperature.")
else: 
    print("Error: Please enter a valid temperature (numeric value).")


# In[ ]:





# In[ ]:




