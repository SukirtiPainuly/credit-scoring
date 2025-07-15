# credit-scoring
#DeFi Wallet Credit Scoring (Aave V2)

This project builds a machine learning model that assigns a **credit score (0 to 1000)** to each DeFi wallet address based on its transaction behavior on the Aave V2 protocol.

---

#Objective

To help DeFi protocols assess wallet trustworthiness using historical activity and behavior patterns, such as how frequently users borrow, repay, or get liquidated.

---

#Dataset

- **Source**: Aave V2 protocol on Polygon
- **Format**: JSON (`user-wallet-transactions.json`)
- **Volume**: 100,000 transaction records across 9 machine-action types
- **Period**: May 2021

---

#Architecture

```text
Raw JSON Data (87MB)
      ↓
load_transactions()
      ↓
extract_features() → Converts transaction logs into wallet-level features
      ↓
score_wallets() → Assigns credit scores using MinMaxScaler (range 0–1000)
      ↓
Output CSV/DF → wallet, credit_score



#Feature Engineering
Each wallet's historical usage is captured via:

Total number of transactions

Count of deposit, borrow, repay, redeem, and liquidationcall

Total deposited and borrowed volume in USD

Net flow of assets

Risk flags like frequent liquidations or missing repayments

#Scoring Logic
A raw_score is calculated using a weighted linear formula:


raw_score = (
    + 1.5 * repay_count
    + 1.2 * deposit_count
    - 2.0 * liquidation_count
    - 1.0 * borrow_count (if not repaid)
)
Then scaled with MinMaxScaler to 0–1000 range.

#Output
Each wallet receives a score:


wallet                                     | credit_score
------------------------------------------|---------------
0x00000000001accfa9cef68cf5371a23025b6d4b6 | 42.13
0x0000000002032370b971dabd36d72f3e5a7bf1ee | 45.84




aave-credit-scoring
│
├── data/
│   └── user-wallet-transactions.json
├── notebooks/
│   └── EDA.ipynb
├── scripts/
│   ├── features.py
│   └── score.py
├── README.md
└── analysis.md

#How to Run

# Set up environment
pip install -r requirements.txt

# Run main notebook
jupyter notebook notebooks/EDA.ipynb
