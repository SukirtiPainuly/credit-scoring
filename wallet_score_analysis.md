# Credit Score Analysis Report

This document summarizes the analysis of wallet behavior and credit scoring from Aave V2 transaction data. Each wallet was assigned a credit score between **0 and 1000**, based on its historical usage patterns.

---

# Score Distribution

We categorized the wallets into **score buckets** to understand behavioral patterns:

| Score Range | Number of Wallets | Percentage | Behavior Description                           |
| ----------- | ----------------- | ---------- | ---------------------------------------------- |
| 0 - 100     | 130               | 3.7%       | Highly risky: frequent liquidations, no repays |
| 100 - 200   | 370               | 10.5%      | Risky: low repays, high borrow, inconsistent   |
| 200 - 300   | 620               | 17.7%      | Sub-optimal: some deposits, few repayments     |
| 300 - 400   | 720               | 20.6%      | Emerging: better patterns, minimal risk        |
| 400 - 500   | 580               | 16.6%      | Average users with moderate consistency        |
| 500 - 600   | 500               | 14.3%      | Good behavior: repay > borrow, steady deposit  |
| 600 - 700   | 320               | 9.1%       | Very good: healthy borrow/repay habits         |
| 700 - 800   | 160               | 4.6%       | Responsible: safe usage, consistent patterns   |
| 800 - 900   | 70                | 2.0%       | Trusted: high deposits, timely repays          |
| 900 - 1000  | 27                | 0.8%       | Ideal: reliable, never liquidated              |


---

# Behavioral Insights

# Wallets in Lower Range (0-300):

- Common behavior:
  - Rarely repay borrowed assets
  - Frequently liquidated
  - Very low deposit volume
- Risk factors:
  - Likely to be exploiters or low-trust participants
  - Inconsistent usage with spikes of borrow

# Wallets in Higher Range (700-1000):

- Common behavior:
  - Regular deposits
  - Balanced borrow-to-repay ratio
  - No or very few liquidation events
  - Long-term consistent interaction with Aave

---

# Visual Representation


```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.hist(scored_df['credit_score'], bins=10, range=(0,1000), edgecolor='black')
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Wallet Count")
plt.grid(True)
plt.savefig("credit_score_distribution.png")
plt.show()
```

---

# Final Takeaway

The scoring model effectively captures behavioral diversity. This report can help DeFi platforms:

- Detect high-risk wallets for monitoring
- Promote safe users with loyalty rewards or better rates
- Maintain transparency and trust in the ecosystem


