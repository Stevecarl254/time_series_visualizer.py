
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data: Remove outliers
data = data[(data['value'] >= data['value'].quantile(0.025)) & (data['value'] <= data['value'].quantile(0.975))]

# Create a line plot of the data
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['value'], color='blue', label='Page Views', linewidth=2)
plt.title('Daily Page Views of freeCodeCamp Forum (2016-2019)')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('line_plot.png')
plt.show()

# Create a bar chart of monthly averages
monthly_data = data.resample('M').mean()

plt.figure(figsize=(12, 6))
monthly_data['value'].plot(kind='bar', color='orange')
plt.title('Monthly Average Page Views')
plt.ylabel('Average Page Views')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# Create box plots for yearly data
data['year'] = data.index.year
plt.figure(figsize=(12, 6))
sns.boxplot(x='year', y='value', data=data.reset_index())
plt.title('Yearly Distribution of Page Views')
plt.ylabel('Page Views')
plt.xlabel('Year')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('box_plot.png')
plt.show()
```
