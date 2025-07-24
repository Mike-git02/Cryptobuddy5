
---

### ✅ `cryptobot.py`

```python
# CryptoBuddy - Your AI-Powered Financial Sidekick! 🌟

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Try {recommend}! It’s eco-friendly and has long-term potential."
    
    elif "trending" in user_query or "growth" in user_query or "profitable" in user_query:
        best = None
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                best = coin
                break
        return f"🚀 {best} is on the rise and highly profitable right now!" if best else "No top-performing coin found."

    elif "energy" in user_query:
        low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"🔋 Low energy cryptos: {', '.join(low_energy)}" if low_energy else "No low energy cryptos found."

    elif "all" in user_query or "list" in user_query:
        return f"📊 Available coins: {', '.join(crypto_db.keys())}"

    else:
        return "🤖 I didn’t understand that. Try asking about sustainability, profitability, or energy use."

# ---- Chat loop ----
print("💬 Welcome to CryptoBuddy! Ask me about crypto trends, sustainability, or profits.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Goodbye and happy investing! 💸")
        break
    response = respond_to_query(user_input)
    print(f"CryptoBuddy: {response}")
