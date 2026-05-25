import pandas as pd

data = {
    "country": ["Mexico"],
    "population": [128000000],
    "total_cases": [7702809],
    "total_deaths": [334958],
    "recovered": [6899865]
}

df = pd.DataFrame(data)

df["infection_rate_pct"] = (df["total_cases"] / df["population"]) * 100
df["death_rate_pct"] = (df["total_deaths"] / df["population"]) * 100
df["recovery_rate_pct"] = (df["recovered"] / df["total_cases"]) * 100

print(df)

print("\nSummary:")
print(f"Population: {df.loc[0, 'population']:,}")
print(f"Total Cases: {df.loc[0, 'total_cases']:,}")
print(f"Total Deaths: {df.loc[0, 'total_deaths']:,}")
print(f"Infection Rate: {df.loc[0, 'infection_rate_pct']:.2f}%")
print(f"Death Rate: {df.loc[0, 'death_rate_pct']:.2f}%")
print(f"Recovery Rate: {df.loc[0, 'recovery_rate_pct']:.2f}%")