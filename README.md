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


