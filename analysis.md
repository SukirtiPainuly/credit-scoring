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
