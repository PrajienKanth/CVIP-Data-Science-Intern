import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:/Users/Tharaneetharan/Downloads/terroism.csv', encoding='latin1')


# Basic data exploration
def basic_data_exploration():
    print(df.head())
    print(df.info())
    print(df.describe())

# Data visualization: Number of attacks by region
def visualize_attacks_by_region():
    plt.figure(figsize=(12, 6))
    sns.countplot(x='region_txt', data=df, order=df['region_txt'].value_counts().index)
    plt.xticks(rotation=90)
    plt.title('Number of Attacks by Region')
    plt.show()


# Time trends analysis
def analyze_time_trends():
    # Convert the 'iyear' column to integer
    df['iyear'] = df['iyear'].astype(int)

    # Group the data by year and count the number of attacks in each year
    year_counts = df['iyear'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=year_counts.index, y=year_counts.values)
    plt.title('Terrorism Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Attacks')

    # Set x-axis ticks to be all the years present in the dataset
    plt.xticks(year_counts.index, rotation=45)  # Rotate x-axis labels for readability if necessary

    plt.grid(True)
    plt.show()



# High-risk areas analysis
def analyze_high_risk_areas():
    high_risk_countries = df['country_txt'].value_counts().head(10)

    # Create a donut chart
    plt.figure(figsize=(8, 8))
    plt.pie(high_risk_countries, labels=high_risk_countries.index, autopct='%1.1f%%', wedgeprops=dict(width=0.4))
    plt.title('Top 10 High-Risk Countries')
    plt.show()


# Factors contributing to terrorism
def analyze_factors_contributing():
    sns.countplot(x='weaptype1_txt', hue='success', data=df)
    plt.xticks(rotation=90)
    plt.title('Weapon Type vs. Attack Success')
    plt.show()


# Option-to-method mapping
analysis_options = {
    '1': basic_data_exploration,
    '2': visualize_attacks_by_region,
    '3': analyze_time_trends,
    '4': analyze_high_risk_areas,
    '5': analyze_factors_contributing,
}

while True:
    # Offer options for analysis methods within the loop
    print("Choose an analysis option:")
    print("1: Basic Data Exploration")
    print("2: Visualize Attacks by Region")
    print("3: Time Trends")
    print("4: Identify High-Risk Region")
    print("5: Reveal Factors Contributing to Terrorism")
    print("6: Exit")

    analysis_option = input("Choose The option: ")

    if analysis_option == '6':
        break

    if analysis_option in analysis_options:
        analysis_options[analysis_option]()
    else:
        print("Invalid option. Please choose a valid numerical option or '6' to exit.")
