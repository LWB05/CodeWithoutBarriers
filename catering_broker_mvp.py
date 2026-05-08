import time
import random
import yfinance as yf # NEW: We use Yahoo Finance for real data

# ==========================================
# 1. THE DATABASE (Real Market Mapping)
# ==========================================
# We map ingredients to real Yahoo Finance Agricultural Futures tickers.
# LE=F (Live Cattle), HE=F (Lean Hogs/Pork), ZC=F (Corn)
COMMODITY_MAP = {
    "premium_beef": {"ticker": "LE=F", "substitute": "pork_cuts"},
    "pork_cuts": {"ticker": "HE=F", "substitute": None},
    "vegetable_base": {"ticker": "ZC=F", "substitute": None}
}

# Simulated Recipe Book
RECIPES = {
    "beef_stew": ["premium_beef", "vegetable_base"],
    "pork_stew": ["pork_cuts", "vegetable_base"]
}

# ==========================================
# 2. THE AGENTS
# ==========================================

class RecipeAnalyzerAgent:
    """Agent that breaks down client orders into raw ingredients."""
    
    def __init__(self):
        self.name = "[Recipe Analyzer]"

    def breakdown_order(self, dish_name):
        print(f"\n{self.name} Analyzing order for: '{dish_name}'...")
        time.sleep(1)
        
        if dish_name not in RECIPES:
            print(f"❌ {self.name} Unknown dish.")
            return None
            
        ingredients = RECIPES[dish_name]
        print(f"✅ {self.name} Extracted required ingredients: {ingredients}")
        return ingredients


class MarketBrokerAgent:
    """Fintech-style Agent that buys ingredients and optimizes margins."""
    
    def __init__(self):
        self.name = "[Market Broker]"

    def get_real_price(self, ticker_symbol):
        """Fetches real live market data from Yahoo Finance."""
        print(f"  📡 Fetching live market data for {ticker_symbol}...")
        try:
            # Fetch the last 2 days of market data
            ticker = yf.Ticker(ticker_symbol)
            hist = ticker.history(period="2d") 
            
            if len(hist) < 2:
                return 15.00, "STABLE" # Fallback if market just closed/opened
                
            yesterday_close = hist['Close'].iloc[0]
            current_price = hist['Close'].iloc[1]
            
            # If price went up by more than 0.2% today, flag it as SPIKING
            percent_change = (current_price - yesterday_close) / yesterday_close
            status = "SPIKING" if percent_change > 0.002 else "STABLE"
            
            return current_price, status
        except Exception:
            # Fallback in case of no internet
            return 15.00, "STABLE" 

    def procure_ingredients(self, ingredient_list):
        print(f"\n{self.name} Scanning real global wholesale futures markets...")
        time.sleep(1)
        
        total_cost = 0
        final_basket = []
        
        for item in ingredient_list:
            if item not in COMMODITY_MAP:
                continue
                
            ticker = COMMODITY_MAP[item]["ticker"]
            current_price, status = self.get_real_price(ticker)
            
            # If the price is spiking, the agent autonomously finds a cheaper substitute
            if status == "SPIKING" and COMMODITY_MAP[item]["substitute"]:
                sub = COMMODITY_MAP[item]["substitute"]
                sub_ticker = COMMODITY_MAP[sub]["ticker"]
                
                print(f"  ⚠️ ALERT: {item.upper()} ({ticker}) is SPIKING (${current_price:.2f}).")
                
                # Fetch real price of substitute
                sub_price, sub_status = self.get_real_price(sub_ticker)
                print(f"  🔄 SWAPPING: Brokering deal for {sub.upper()} ({sub_ticker}) instead (${sub_price:.2f}).")
                
                total_cost += sub_price
                final_basket.append(sub)
            else:
                print(f"  🛒 PURCHASING: {item} ({ticker}) at stable price (${current_price:.2f}).")
                total_cost += current_price
                final_basket.append(item)
                
            time.sleep(0.5)
            
        print(f"\n✅ {self.name} Procurement Complete.")
        print(f"   Final Cost: ${total_cost:.2f}")
        print(f"   Optimized Basket: {final_basket}")


# ==========================================
# 3. THE MAIN WORKFLOW
# ==========================================
def main():
    print("=========================================================")
    print("📈 AI CATERING BROKER: LIVE PROCUREMENT FEED INITIALIZED 📈")
    print("=========================================================\n")
    
    analyzer_bot = RecipeAnalyzerAgent()
    broker_bot = MarketBrokerAgent()
    
    # Run the workflow for a Beef Stew order
    print("--- NEW CATERING CONTRACT RECEIVED ---")
    dish_requested = "beef_stew"
    
    # 1. Analyzer breaks it down
    required_ingredients = analyzer_bot.breakdown_order(dish_requested)
    
    if required_ingredients:
        # 2. Broker buys and optimizes
        broker_bot.procure_ingredients(required_ingredients)

if __name__ == "__main__":
    main()
