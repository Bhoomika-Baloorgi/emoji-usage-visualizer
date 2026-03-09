# Emoji Usage Visualizer

## Overview
Emoji Usage Visualizer is a simple Python project that analyzes emoji usage in a text file.  
The program reads a sample text dataset containing messages with emojis, extracts the emojis present in the text, and calculates how frequently each emoji appears.  
The results are then visualized using a bar chart to help understand emoji usage patterns in the dataset.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Dataset
The project uses a small sample text dataset that contains lines of text with emojis.  
Each line represents a short message containing one or more emojis.  
The dataset is used to demonstrate how emoji characters can be extracted and analyzed from text data.

## Features
- Reads text data containing emojis
- Extracts emojis from the text
- Calculates frequency of each emoji
- Generates a visualization showing emoji usage

## Project Structure
emoji-usage-visualizer  
│  
├── dataset.txt  
├── emoji_analysis.py  
├── output_chart.png  
├── requirements.txt  
└── README.md  

## How to Run

1. Clone the repository

git clone https://github.com/Bhoomika-Baloorgi/emoji-usage-visualizer.git

2. Move into the project folder

cd emoji-usage-visualizer

3. Install dependencies

pip install -r requirements.txt

4. Run the script

python emoji_analysis.py

## Output
The script generates a bar chart that visualizes the frequency of emojis found in the dataset.

## Purpose
This project demonstrates basic data processing and visualization using Python.  
It shows how emoji characters can be extracted from text and analyzed to identify simple usage patterns.
