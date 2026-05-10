## The Problem

Traditional catering SMEs operate on razor-thin margins and are highly vulnerable to daily price spikes in wholesale food commodities. Managing these costs dynamically is nearly impossible with static menus and traditional supply chain management. A sudden spike in beef or poultry prices can wipe out the profit margin of an entire event.

## My Solution

I built **MarginGuard**, an Agentic Procurement Broker that treats catering supply chains like a dynamic financial market.

Instead of static purchasing, my multi-agent system breaks down catering orders into raw commodities and monitors the global Agricultural Futures market in real-time. If a required ingredient experiences a sudden market spike, my agent autonomously intervenes, calculating and brokering a purchase for a pre-approved, cost-effective substitute. This ensures seamless catering operations while actively protecting the SME's profit margins.

## Multi-Agent Architecture (Local MVP)

My current prototype operates using a lightweight, scalable Python architecture featuring two distinct agents:

1. **Recipe Analyzer Agent:** Parses high-level catering requests (e.g., "Beef Stew") and cross-references external JSON databases to structure them into raw commodity requirements.

2. **Market Broker Agent:** Connects to real-time financial market data (`yfinance`), analyzes 48-hour trailing price histories to detect market spikes, and executes optimized procurement logic with autonomous substitutions.

## Microsoft Azure Cloud Architecture (Production Ready)

*As per the hackathon's architectural guidelines, this system is explicitly designed using an Azure-ready interface. The local prototype acts as a proof-of-concept for the following Azure-native deployment:*

* **Azure OpenAI Service (Cognitive Reasoning):** In production, the Recipe Analyzer Agent will utilize Azure OpenAI to parse complex, unstructured client dietary requests and dynamically generate structured JSON commodity schemas.

* **Azure Functions (Event-Driven Brokerage):** The Market Broker Agent is designed for deployment as an Azure Function. Catering orders are highly variable; Azure Functions allow the broker logic to scale up instantly during high-volume wholesale trading hours, and scale down to zero during off-hours.

* **Azure Cosmos DB (Dynamic Matrix Storage):** The `COMMODITY_MAP` and substitution matrices (currently simulated via local JSON files) are structured for migration to Azure Cosmos DB. This ensures single-digit millisecond latency when the Broker Agent queries live alternatives during a market spike.

## How to Run the Prototype Locally

**1. Clone the repository:**

```
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name

```

**2. Install dependencies:**
The system uses `yfinance` to pull live data from the global stock market.

```
pip install yfinance

```

**3. Run the multi-agent system:**

```
python catering_broker_mvp.py

```

## Repository Structure

```
├── catering_broker_mvp.py   # Main multi-agent execution script
├── commodities.json         # Simulated Cosmos DB market mapping
├── recipes.json             # Simulated client menu database
├── README.md                # Project documentation
└── .gitignore               # System ignore file

```
