# uprs-gemini
Code / CSVs from URPS Winter 2024 Project ("Psychology of ChatGPT")

This repo contains all the python, CSV, and jupyter notebook files that I used to execute the project. The repo is broken into folders for each of the experiments conducted:
1. Doctors - Framing Effect: this experiment presents medical information in 2 ways (same information) and asks Gemini to choose a treatment 
3. Pythons - Logic Question: this experiment asks a logic question/riddle with 8 variations and asks Gemini to answer true/false to three statements  
4. Basketball - Racial Bias: this experiment presents a description of a basketball along with their race and asks Gemini to return a summary 
5. Gemini Blocks -> this folder is broken into 3 folders for the 3 sub-experiments conducted: each recorded which/how many calls were blocked
   4a. Sexually Explicit Stories: this subexperiment asked Gemini to write stories about a relationship between 2 people 
   4b. Dangerous Stories: this subexperiment asked Gemini to write stories about a violent interaction between 2 people 
   4c. Medical Questions: this subexperiment asked Gemini to provide help/advice for a medical issue 

Each experiment has the intial .py files, which call the Gemini API in a loop to collect the response data. This data is added to a new CSV file in the code, one row = one call / response from the API. Any CSVs which were created are in the folder. Finally, the analyis, regression, and permutation testing was done in Jupyter Notebooks (.ipynb) files, for which each (sub)folder has 1. 
