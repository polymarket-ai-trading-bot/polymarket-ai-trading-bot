import os
from dotenv import load_dotenv
from polymarket_api import get_markets
from agent import analyze_event
from strategy import expected_value, kelly_fraction

load_dotenv()

def main():
    print("🤖 Polymarket AI Agent Starting...\n")
    markets = get_markets(limit=5)

    for _, row in markets.iterrows():
        q = row["question"]
        prices = row["outcomePrices"]
        market_prob = float(prices[0]) if prices else 0.5

        ai_prob = analyze_event(q, ["YES", "NO"])
        ev = expected_value(ai_prob, market_prob)
        kelly = kelly_fraction(ai_prob, 2.0)

        print(f"🎯 {q}")
        print(f" - Market prob: {market_prob:.2f}")
        print(f" - AI prob: {ai_prob:.2f}")
        print(f" - EV: {ev:+.3f} | Kelly fraction: {kelly:.3f}")
        print("-" * 50)

if __name__ == "__main__":
    main()
