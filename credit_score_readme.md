#  Aave V2 DeFi Wallet Credit Scoring

This repository presents a complete pipeline to score wallets on the Aave V2 protocol with a credit score between **0 and 1000**, based on historical transaction behavior such as `deposit`, `borrow`, `repay`, `redeem`, and `liquidationcall`.

---

# Objective

Assign a numerical credit score to each wallet to:

- Quantify the trustworthiness of DeFi participants
- Help DeFi protocols assess lending risk and reward consistency
- Detect risky/bot-like behavior in historical logs

---

# Project Structure

```
aave-credit-scoring/
├── data/
│   └── user-wallet-transactions.json         # Raw transaction data
├── scripts/
│   ├── features.py                           # Feature extraction logic
│   └── score.py                              # Scoring methodology
├── notebooks/
│   └── EDA.ipynb                             # Exploratory data + scoring demo
├── analysis.md                               # Score bucket insights and charts
├── README.md                                 # You're here ✅
```

---

# Data Input

- JSON File: `user-wallet-transactions.json`
- Format: One record per transaction with fields like `userWallet`, `action`, `timestamp`, `actionData.amount`, etc.
- Size: \~100,000 transactions

---

# Pipeline Flow

1. **Load Raw JSON** using `load_transactions()`
2. **Aggregate Wallet Behavior** with `extract_features()`
3. **Score Wallets** using weighted scoring logic in `score_wallets()`
4. **Normalize Scores** to a 0-1000 range with `MinMaxScaler`
5. **Output**: DataFrame with `wallet`, `credit_score`

---

# Scoring Formula

```python
raw_score = (
    1.5 * repay_count +
    1.2 * deposit_count -
    2.0 * liquidation_count -
    1.0 * borrow_without_repay
)
```

- Higher weights to repays and deposits
- Penalize frequent liquidations and poor behavior
- Scores are then scaled using `MinMaxScaler` (range: 0–1000)

---

# Feature Highlights

- Total and per-action counts (deposit, borrow, repay, liquidation)
- Average USD volume per wallet
- Net flow: deposits - borrow
- Liquidation frequency
- Borrow without repay flag

---

# Result Example

| wallet                                     | credit\_score |
| ------------------------------------------ | ------------- |
| 0x00000000001accfa9cef68cf5371a23025b6d4b6 | 41.91         |
| 0x0000000002032370b971dabd36d72f3e5a7bf1ee | 45.84         |

See full behavioral analysis in [wallet_score_analysis.md].

---

# Setup Instructions

```bash

$ git clone https://github.com/<your-username>/aave-credit-scoring.git
$ cd aave-credit-scoring

$ pip install -r requirements.txt

$ jupyter notebook notebooks/EDA.ipynb
```

---

# Bonus: Visualize Distribution

Use this snippet in your notebook to plot scores:

```python
import matplotlib.pyplot as plt
plt.hist(scored_df['credit_score'], bins=10, range=(0,1000), edgecolor='black')
plt.title("Credit Score Distribution")
plt.xlabel("Score Bucket")
plt.ylabel("Wallet Count")
plt.grid(True)
plt.show()
```

---

# Contribution

Pull requests and feedback welcome! Please open issues for bugs or improvement ideas.

---

# License

This repository is open for non-commercial research and educational use.

---

>  Built by Sukirti Painuly for a DeFi credit scoring challenge to showcase real-world ML + blockchain data analysis.

