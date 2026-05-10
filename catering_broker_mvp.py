import time
import json
import yfinance as yf

# ==========================================
# 1. LOAD EXTERNAL FILES (Simulating Cosmos DB)
# ==========================================
print("Loading databases from external JSON files...")

try:
    with open("commodities.json", "r") as f:
        COMMODITY_MAP = json.load(f)
        
    with open("recipes.json", "r") as f:
        RECIPES = json.load(f)
        
    print("Databases successfully loaded!\n")
except FileNotFoundError:
    print("ERROR: Could not find recipes.json or commodities.json. Please ensure they are in the same folder.")
    exit()

# ==========================================
# 2. THE AGENTS
# ==========================================

class RecipeAnalyzerAgent:
    """Agent that breaks down client orders into raw ingredients."""
    
    def __init__(self):
        self.name = "[Recipe Analyzer]"

    def breakdown_order(self, dish_name):
        print(f"{self.name} Analyzing order for: '{dish_name}'...")
        time.sleep(1)
        
        if dish_name not in RECIPES:
            print(f"{self.name} ERROR: Unknown dish.")
            return None
            
        ingredients = RECIPES[dish_name]
        print(f"{self.name} SUCCESS: Extracted required ingredients: {ingredients}")
        return ingredients


class MarketBrokerAgent:
    """Fintech-style Agent that buys ingredients and optimizes margins."""
    
    def __init__(self):
        self.name = "[Market Broker]"

    def get_real_price(self, ticker_symbol):
        """Fetches real live market data from Yahoo Finance."""
        print(f"  Fetching live market data for {ticker_symbol}...")
        try:
            ticker = yf.Ticker(ticker_symbol)
            hist = ticker.history(period="2d") 
            
            if len(hist) < 2:
                return 15.00, "STABLE" 
                
            yesterday_close = hist['Close'].iloc[0]
            current_price = hist['Close'].iloc[1]
            
            percent_change = (current_price - yesterday_close) / yesterday_close
            status = "SPIKING" if percent_change > 0.002 else "STABLE"
            
            return current_price, status
        except Exception:
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
            
            if status == "SPIKING" and COMMODITY_MAP[item]["substitute"]:
                sub = COMMODITY_MAP[item]["substitute"]
                sub_ticker = COMMODITY_MAP[sub]["ticker"]
                
                print(f"  ALERT: {item.upper()} ({ticker}) is SPIKING (${current_price:.2f}).")
                
                sub_price, sub_status = self.get_real_price(sub_ticker)
                print(f"
