
import numpy as np
import matplotlib.pyplot as plt

initial_capital = 100000
days = 252
simulations = 10000

daily_returns = 0.50 / 252
daily_vol = 0.80 / np.sqrt(252)

random_returns = np.random.normal(daily_returns, daily_vol, (days, simulations))
price_paths = initial_capital*np.exp(np.cumsum(random_returns, axis=0))
random_returns


final_values = price_paths[-1, :]


print("Median Outcome: ${np.median(final_values):,.0f}")
print(f"5% worst case VaR: ₹{np.percentile(final_values, 5):,.0f}")
print(f"Probability of >2L: {np.mean(final_values > 200000)*100:.1f}%")

plt.figure(figsize=(10,6))
plt.hist(final_values/100000, bins=50, alpha=0.7)
plt.axvline(1, color='red', linestyle='--', label='Break-even')
plt.xlabel('Portfolio Value (in Lakhs)')
plt.ylabel('Frequency')
plt.title("Monte Carlo: 1L in BTC after 1 Year - 10,000 Simulations")
plt.legend()
plt.show()
          
