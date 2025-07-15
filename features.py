import json
import pandas as pd
from collections import defaultdict

def load_transactions(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def extract_features(data):
    wallet_stats = defaultdict(lambda: {
        "total_txn": 0,
        "deposit_count": 0,
        "borrow_count": 0,
        "repay_count": 0,
        "redeem_count": 0,
        "liquidation_count": 0,
        "total_usd_deposit": 0.0,
        "total_usd_borrow": 0.0,
        "net_usd_flow": 0.0
    })

    for txn in data:
        wallet = txn["userWallet"]
        action = txn["action"]
        stats = wallet_stats[wallet]
        stats["total_txn"] += 1

        if action == "deposit":
            stats["deposit_count"] += 1
            usd = float(txn["actionData"]["amount"]) * float(txn["actionData"]["assetPriceUSD"]) / 1e6
            stats["total_usd_deposit"] += usd
            stats["net_usd_flow"] += usd

        elif action == "borrow":
            stats["borrow_count"] += 1
            usd = float(txn["actionData"]["amount"]) * float(txn["actionData"]["assetPriceUSD"]) / 1e6
            stats["total_usd_borrow"] += usd
            stats["net_usd_flow"] -= usd

        elif action == "repay":
            stats["repay_count"] += 1

        elif action == "redeemunderlying":
            stats["redeem_count"] += 1

        elif action == "liquidationcall":
            stats["liquidation_count"] += 1

    return pd.DataFrame.from_dict(wallet_stats, orient="index")
