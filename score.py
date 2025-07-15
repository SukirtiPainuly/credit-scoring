import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def score_wallets(df):
    df = df.copy()

    
    df["net_flow_usd"] = df["total_usd_deposit"] - df["total_usd_borrow"]


    df["raw_score"] = (
        df["deposit_count"] * 2 +
        df["repay_count"] * 3 +
        df["total_usd_deposit"] * 0.00001 +
        df["net_flow_usd"] * 0.00001 -
        df["liquidation_count"] * 5
    )


    scaler = MinMaxScaler(feature_range=(0, 1000))
    df["credit_score"] = scaler.fit_transform(df[["raw_score"]])

    return df[["wallet", "credit_score"]]
