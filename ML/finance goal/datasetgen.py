import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic dataset
def generate_financial_dataset(num_samples=1000):
    age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
    income_ranges = ['Low', 'Medium-Low', 'Medium', 'Medium-High', 'High']
    goals = ['Retirement', 'Home Purchase', 'Education', 'Wealth Accumulation', 'Short-term Savings']
    risk_levels = ['Conservative', 'Moderate-Conservative', 'Balanced', 'Moderate-Aggressive', 'Aggressive']
    investment_types = ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency']

    def generate_portfolio_allocation():
        total = 100
        allocations = []
        for _ in range(len(investment_types) - 1):
            allocation = random.randint(0, total)
            allocations.append(allocation)
            total -= allocation
        allocations.append(total)
        return dict(zip(investment_types, allocations))

    data = {
        'UserID': range(1, num_samples + 1),
        'Age_Group': np.random.choice(age_groups, num_samples),
        'Income_Level': np.random.choice(income_ranges, num_samples),
        'Primary_Financial_Goal': np.random.choice(goals, num_samples),
        'Risk_Tolerance': np.random.choice(risk_levels, num_samples)
    }

    portfolio_data = [generate_portfolio_allocation() for _ in range(num_samples)]
    portfolio_df = pd.DataFrame(portfolio_data)
    df = pd.DataFrame(data)
    df = pd.concat([df, portfolio_df], axis=1)

    def assign_investment_strategy(row):
        if row['Risk_Tolerance'] == 'Conservative':
            return 'Low-Risk Preservation'
        elif row['Risk_Tolerance'] == 'Moderate-Conservative':
            return 'Conservative Growth'
        elif row['Risk_Tolerance'] == 'Balanced':
            return 'Balanced Growth'
        elif row['Risk_Tolerance'] == 'Moderate-Aggressive':
            return 'Aggressive Growth'
        else:
            return 'High-Risk Aggressive'

    df['Recommended_Strategy'] = df.apply(assign_investment_strategy, axis=1)
    return df

# Generate and save the dataset
financial_dataset = generate_financial_dataset(1000)
financial_dataset.to_csv('financial_goals_dataset.csv', index=False)
