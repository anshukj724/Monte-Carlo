<img width="867" height="545" alt="download" src="https://github.com/user-attachments/assets/b90f9e8d-362a-4387-937a-8b85ca162088" />
# 📊 Monte Carlo Bitcoin Simulation



## 🚀 Overview

This project simulates how an initial investment of ₹1,00,000 could grow over 1 year using a **Monte Carlo simulation**.
It models possible price paths based on expected return and volatility, helping visualize risk and uncertainty.

---

## ⚙️ Parameters

* Initial Capital: ₹1,00,000
* Time Horizon: 252 trading days (~1 year)
* Simulations: 10,000
* Expected Return: 50% annually
* Volatility: 80% annually

---

## 📈 What the Graph Shows

The histogram represents **final portfolio values** after 1 year across 10,000 simulations.

* Each bar = number of outcomes in that range
* X-axis = portfolio value (relative to ₹1L)
* Red dashed line = **break-even point (₹1L)**

### 🧠 How to read it:

* Right side (above 1) → profit scenarios
* Left side (below 1) → loss scenarios
* Wide spread → high volatility (big uncertainty)
* Peak area → most likely outcomes

---

## 📊 Key Metrics

*Median Outcome: ${np.median(final_values):,.0f}
*5% worst case VaR: ₹43,283
*Probability of >2L: 41.3%


---

## 💡 Insight

This simulation shows that even with high expected returns, outcomes vary widely due to volatility—highlighting both **risk and opportunity** in crypto investments.

---
