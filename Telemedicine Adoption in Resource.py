# ***Telemedicine Adoption in Resource Allocation: Exploring how telemedicine can optimize healthcare resource allocation, especially in rural or underserved areas.***

import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt


# Load the datasets
covid_df = pd.read_csv('covid19.csv')
data_df = pd.read_csv('data.csv')
telemedicine_df = pd.read_csv('telemedicine_use.csv')

# Explore the first few rows of each dataset
print("COVID-19 Dataset:")
print(covid_df.head())

print("\nData Dataset:")
print(data_df.head())

print("\nTelemedicine Use Dataset:")
print(telemedicine_df.head())

#Explore the impact of COVID-19 on healthcare resource allocation  
# Assuming you have loaded your datasets
data_df = pd.read_csv('data.csv')
telemedicine_df = pd.read_csv('telemedicine_use.csv')

# Merge datasets based on common columns
merged_df = pd.merge(data_df, telemedicine_df, on=['Indicator', 'Group', 'State', 'Subgroup', 'Phase', 'Time Period', 'Time Period Label', 'Time Period Start Date', 'Time Period End Date'], how='inner')

# Filter relevant columns for analysis
analysis_columns = ['Indicator', 'Group', 'State', 'Subgroup', 'Phase', 'Time Period', 'Time Period Label', 'Time Period Start Date', 'Time Period End Date', 'Value_x', 'Value_y']
merged_df = merged_df[analysis_columns]

# Rename columns for better understanding
merged_df = merged_df.rename(columns={'Value_x': 'Healthcare_Resource_Allocation', 'Value_y': 'Telemedicine_Usage'})

# Convert 'Time Period Start Date' to datetime for proper sorting
merged_df['Time Period Start Date'] = pd.to_datetime(merged_df['Time Period Start Date'])

# Sort the DataFrame by 'Time Period Start Date'
merged_df = merged_df.sort_values(by='Time Period Start Date')

# Plot the trends over time
plt.figure(figsize=(12, 6))
plt.plot(merged_df['Time Period Start Date'], merged_df['Healthcare_Resource_Allocation'], label='Healthcare Resource Allocation')
plt.plot(merged_df['Time Period Start Date'], merged_df['Telemedicine_Usage'], label='Telemedicine Usage')
plt.title('Impact of COVID-19 on Healthcare Resource Allocation and Telemedicine Usage Over Time')
plt.xlabel('Time Period Start Date')
plt.ylabel('Value')
plt.legend()
plt.show()


from wordcloud import WordCloud

# Assuming you have a DataFrame named 'swot_data' with relevant data
# You might need to adjust this based on your actual dataset

# Sample data for illustration purposes
data = {
    'Category': ['Strengths', 'Weaknesses', 'Opportunities', 'Threats'],
    'Factors': [
        'Cutting-edge technologies',
        'Uncertainties in telemedicine adoption',
        'Rising healthcare costs',
        'Regulatory uncertainties'
    ]
}

swot_data = pd.DataFrame(data)

# Word cloud for visualizing SWOT factors
def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Extract factors for each SWOT category
strengths = ' '.join(swot_data[swot_data['Category'] == 'Strengths']['Factors'])
weaknesses = ' '.join(swot_data[swot_data['Category'] == 'Weaknesses']['Factors'])
opportunities = ' '.join(swot_data[swot_data['Category'] == 'Opportunities']['Factors'])
threats = ' '.join(swot_data[swot_data['Category'] == 'Threats']['Factors'])

# Generate word clouds for each SWOT category
generate_wordcloud(strengths, 'Strengths')
generate_wordcloud(weaknesses, 'Weaknesses')
generate_wordcloud(opportunities, 'Opportunities')
generate_wordcloud(threats, 'Threats')


import seaborn as sns

# Assuming you have a dataset with relevant columns (e.g., 'Location', 'Access to Healthcare Score', 'Income', 'Rural Status', etc.)
# Replace 'your_dataset.csv' with the actual filename

dataset = pd.read_csv('telemedicine_use.csv')
print(dataset.head())
summary_stats = dataset.describe()
print(summary_stats)

# Visualize access to healthcare based on income and rural status
plt.figure(figsize=(12, 6))

# Example: Boxplot to show the distribution of access to healthcare based on income and rural status
sns.boxplot(x='Income', y='Access to Healthcare Score', hue='Rural Status', data=dataset)
plt.title('Access to Healthcare Based on Income and Rural Status')
plt.xlabel('Income')
plt.ylabel('Access to Healthcare Score')
plt.show()

# Example: Pairplot to explore correlations among variables
sns.pairplot(dataset[['Access to Healthcare Score', 'Income', 'Rural Status']])
plt.show()

# Correlation analysis
correlation_matrix = dataset[['Access to Healthcare Score', 'Income', 'Rural Status']].corr()
print(correlation_matrix)

file_path_covid19 = 'covid19.csv'

# Read the file to see the initial few rows and understand its structure
try:
    covid19_data = pd.read_csv(file_path_covid19)
    covid19_data_head = covid19_data.head()
except Exception as e:
    covid19_data_head = str(e)

covid19_data_head

file_path_telemedicine = 'telemedicine_use.csv'

# Read the file to see the initial few rows and understand its structure
try:
    telemedicine_data = pd.read_csv(file_path_telemedicine)
    telemedicine_data_head = telemedicine_data.head()
except Exception as e:
    telemedicine_data_head = str(e)

telemedicine_data_head

# Analyzing the impact of telemedicine on healthcare access in different demographics
# We will focus on the 'telemedicine_use.csv' data as it seems most relevant for this analysis.
# First, let's examine the structure of this data in more detail.
telemedicine_data.info()
# Since the data includes time periods and different demographics,
# we can analyze how telemedicine usage varied across different age groups and over time.

# indicator of how healthcare access
sns.set(style="whitegrid")

# Filtering data for national estimates to observe overall trends
national_data = telemedicine_data[telemedicine_data['Group'] == 'National Estimate']

# Plotting telemedicine usage over time
plt.figure(figsize=(15, 7))
sns.lineplot(data=national_data, x='Time Period Label', y='Value')
plt.xticks(rotation=45)
plt.title('Telemedicine Usage Over Time (National Estimate)')
plt.xlabel('Time Period')
plt.ylabel('Value (%)')
plt.tight_layout()
plt.show()

# Next, we'll examine the variation in telemedicine use across different age groups.

# Filtering data for age group comparisons
age_group_data = telemedicine_data[telemedicine_data['Group'] == 'By Age']

# Plotting telemedicine usage across different age groups
plt.figure(figsize=(15, 7))
sns.barplot(data=age_group_data, x='Subgroup', y='Value', ci=None)
plt.title('Telemedicine Usage Across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Value (%)')
plt.tight_layout()
plt.show()


# Filtering data for state-wise comparison to observe potential rural vs. urban differences
state_data = telemedicine_data[telemedicine_data['Group'] == 'By State']

# Due to the large number of states, we'll focus on a subset for visualization
# Selecting a sample of states for analysis
sampled_states = state_data['State'].unique()[:10]
sampled_state_data = state_data[state_data['State'].isin(sampled_states)]

# Plotting telemedicine usage in the sampled states
plt.figure(figsize=(15, 7))
sns.barplot(data=sampled_state_data, x='State', y='Value', ci=None)
plt.title('Telemedicine Usage in Sampled States')
plt.xlabel('State')
plt.ylabel('Value (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# data-driven SWOT analysis

# Analyzing 'telemedicine_use.csv' for strengths and weaknesses
telemedicine_usage_summary = telemedicine_data.describe()

# Checking for trends that could indicate opportunities and threats
# Calculating the average telemedicine use per time period
average_use_per_period = telemedicine_data.groupby('Time Period Label')['Value'].mean()

# Preparing the summary for the SWOT analysis
swot_analysis_data = {
    "Strengths": telemedicine_usage_summary,
    "Opportunities": average_use_per_period
}

swot_analysis_data


# Filtering the dataset for national estimates
national_telemedicine_data = telemedicine_data[telemedicine_data['Group'] == 'National Estimate']

# Converting time period labels to datetime for better plotting
national_telemedicine_data['Time Period Start Date'] = pd.to_datetime(national_telemedicine_data['Time Period Start Date'])
national_telemedicine_data['Time Period End Date'] = pd.to_datetime(national_telemedicine_data['Time Period End Date'])

# Plotting the trend of telemedicine usage over time
plt.figure(figsize=(15, 6))
sns.lineplot(data=national_telemedicine_data, x='Time Period Start Date', y='Value')
plt.title('Trend of Telemedicine Usage Over Time (National Estimate)')
plt.xlabel('Time Period Start Date')
plt.ylabel('Percentage of Telemedicine Usage')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# Analyzing the trend of telemedicine usage during the COVID-19 pandemic period.
# We will focus on the time period of the pandemic and see if there's an increase in telemedicine usage.

# Extracting year from the 'Time Period Start Date' for easier analysis
national_telemedicine_data['Year'] = national_telemedicine_data['Time Period Start Date'].dt.year

# Grouping the data by year to see annual trends
annual_telemedicine_usage = national_telemedicine_data.groupby('Year')['Value'].mean().reset_index()

# Plotting the annual trend of telemedicine usage
plt.figure(figsize=(10, 6))
sns.barplot(data=annual_telemedicine_usage, x='Year', y='Value')
plt.title('Annual Average of Telemedicine Usage (National Estimate)')
plt.xlabel('Year')
plt.ylabel('Average Percentage of Telemedicine Usage')
plt.show()


# Analyzing telemedicine usage across different demographics (focusing on age groups)

# Filtering the data to focus on different age groups
age_group_data = telemedicine_data[telemedicine_data['Group'] == 'By Age']

# Plotting telemedicine usage across different age groups
plt.figure(figsize=(15, 8))
sns.barplot(data=age_group_data, x='Subgroup', y='Value', ci=None)
plt.title('Telemedicine Usage Across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Percentage of Telemedicine Usage')
plt.xticks(rotation=45)
plt.show()

# Analyzing the temporal trends in telemedicine usage using the national_telemedicine_data

# Plotting the trend of telemedicine usage over time again, focusing on the overall trend
plt.figure(figsize=(15, 6))
sns.lineplot(data=national_telemedicine_data, x='Time Period Start Date', y='Value')
plt.title('Trend of Telemedicine Usage Over Time (National Estimate)')
plt.xlabel('Time Period Start Date')
plt.ylabel('Percentage of Telemedicine Usage')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Analyzing telemedicine usage across different states

# Filtering the data to focus on state-level data (excluding the national estimate)
state_telemedicine_data = telemedicine_data[(telemedicine_data['Group'] == 'By State') & (telemedicine_data['Subgroup'] != 'United States')]

# Aggregating data to get average telemedicine usage per state
average_state_usage = state_telemedicine_data.groupby('Subgroup')['Value'].mean().reset_index()

# Sorting the data for better visualization
average_state_usage_sorted = average_state_usage.sort_values(by='Value', ascending=False)

# Plotting telemedicine usage across different states
plt.figure(figsize=(15, 12))
sns.barplot(data=average_state_usage_sorted, y='Subgroup', x='Value', ci=None)
plt.title('Average Telemedicine Usage Across Different States')
plt.xlabel('Average Percentage of Telemedicine Usage')
plt.ylabel('State')
plt.show()

# Re-examining the telemedicine_use.csv dataset with a focus on insights relevant to LMICs.

# Analyzing telemedicine usage across different age groups again, as it might provide insights into accessibility
plt.figure(figsize=(15, 8))
sns.barplot(data=age_group_data, x='Subgroup', y='Value', ci=None)
plt.title('Telemedicine Usage Across Different Age Groups (Potentially Relevant to LMICs)')
plt.xlabel('Age Group')
plt.ylabel('Percentage of Telemedicine Usage')
plt.xticks(rotation=45)
plt.show()

# Displaying key insights from this visualization that might be relevant to LMICs
age_group_insights = """
Key Insights for LMICs:
1. Wide Demographic Reach: Telemedicine is used across various age groups, indicating its potential to serve a diverse population.
2. Accessibility: The ability to engage different age demographics shows its potential for wide accessibility, crucial for LMICs.
3. Potential for Elderly Care: Given the usage among older age groups, telemedicine could play a significant role in managing chronic diseases prevalent in this demographic, which is also a growing concern in many LMICs.
"""

age_group_insights

# Revisiting the telemedicine_use.csv dataset to identify trends or disparities that might indicate barriers or areas for increased awareness

# First, we'll look at state-wise disparities in telemedicine usage
state_disparities = average_state_usage_sorted

# Plotting state-wise disparities in telemedicine usage
plt.figure(figsize=(15, 12))
sns.barplot(data=state_disparities, y='Subgroup', x='Value', ci=None)
plt.title('State-wise Disparities in Telemedicine Usage')
plt.xlabel('Average Percentage of Telemedicine Usage')
plt.ylabel('State')
plt.show()

# Insights regarding potential gaps or areas for increased awareness
state_disparities_insights = """
Insights:
1. Variability in Usage: There's significant variability in telemedicine usage across states, indicating potential disparities in access or awareness.
2. Targeted Awareness Campaigns: States with lower usage might benefit from targeted awareness campaigns, possibly leveraging social media to increase knowledge and acceptance of telemedicine services.
3. Understanding Barriers: Further research is needed to understand the specific barriers in states with lower usage – these could be infrastructural, cultural, or related to policy and regulation.
"""

state_disparities_insights
