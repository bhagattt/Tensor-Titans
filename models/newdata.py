import pandas as pd
import numpy as np

# Define possible categories for each categorical column
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
income_levels = ['0-50k', '50k-100k', '100k-150k', '150k+']
financial_goals = ['Retirement', 'Wealth Accumulation', 'Debt Reduction', 'Education', 'Home Purchase']
risk_tolerances = ['Aggressive', 'Balanced', 'Conservative', 'Moderate-Aggressive', 'Moderate-Conservative']

# Generate synthetic data
num_samples = 1000  # Number of samples to generate
data = {
    'Age_Group': np.random.choice(age_groups, num_samples),
    'Income_Level': np.random.choice(income_levels, num_samples),
    'Primary_Financial_Goal': np.random.choice(financial_goals, num_samples),
    'Risk_Tolerance': np.random.choice(risk_tolerances, num_samples),
    'Stocks': np.random.uniform(0, 1, num_samples),
    'Bonds': np.random.uniform(0, 1, num_samples),
    'Real Estate': np.random.uniform(0, 1, num_samples),
    'Mutual Funds': np.random.uniform(0, 1, num_samples),
    'ETFs': np.random.uniform(0, 1, num_samples),
    'Cryptocurrency': np.random.uniform(0, 1, num_samples),
    'Recommended_Strategy': np.random.choice(['Low-Risk Preservation', 'Conservative Growth', 'Balanced Growth', 'Aggressive Growth', 'High-Risk Aggressive'], num_samples)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('financial_goals_dataset_v2.csv', index=False)
print("New training data saved to 'financial_goals_dataset_v2.csv'.")