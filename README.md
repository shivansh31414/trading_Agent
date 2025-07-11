# 📈 AI-Powered Stock Trading Agents with CrewAI

Welcome to **AI-Trading-Crew**, a cutting-edge multi-agent stock trading system powered by **CrewAI** and **Large Language Models (LLMs)**. This project simulates strategic collaboration between autonomous agents to analyze markets, generate recommendations, execute trades, and evaluate portfolio outcomes.

---

## 🚀 Project Overview

This system leverages CrewAI to orchestrate specialized agents that:
- 📊 Analyze stock trends and sentiments
- 🔍 Recommend trades using dynamic strategies
- 🛒 Simulate trade execution and tracking
- 📉📈 Evaluate risk-adjusted portfolio performance

Agents interact in a structured workflow, reflecting real-world trading environments.

---

## 🔧 Tech Stack

| Component           | Description                                    |
|---------------------|------------------------------------------------|
| 🧠 CrewAI            | Multi-agent LLM framework                      |
| 🐍 Python            | Programming language                           |
| 📡 LangChain        | Prompt-based agent orchestration               |
| 📈 Financial APIs    | Market data ingestion (e.g., Alpha Vantage, Yahoo Finance) |
| 📋 Streamlit (optional) | Interactive UI layer                        |

---

## 🤖 Agent Roles

| Agent Name            | Responsibility                                               |
|------------------------|-------------------------------------------------------------|
| `MarketAnalystAgent`   | Aggregates and interprets financial data and market signals |
| `StrategyAgent`        | Selects trading logic (MACD, RSI, AI-based)                |
| `TradingAgent`         | Executes mock trades and updates portfolio                 |
| `RiskEvaluatorAgent`   | Assesses outcomes, calculates ROI, adjusts strategy        |

---

## 🧠 Features

- CrewAI Role/Task architecture
- Autonomous agent collaboration via LLMs
- Support for multiple trading strategies
- Modular agent design for easy extensions
- Streamlit UI for interaction and visualization *(optional)*

---

## 💻 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/ai-trading-crew.git
cd ai-trading-crew

# Install required packages
pip install -r requirements.txt

# Run the main script
python main.py



├── agents/
│   ├── market_analyst.py
│   ├── strategy_agent.py
│   ├── trading_agent.py
│   └── risk_evaluator.py
├── data/
├── config.py
├── main.py
├── utils/
├── README.md
└── requirements.txt



