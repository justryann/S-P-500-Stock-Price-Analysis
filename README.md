# S&P 500 Stock Price Analysis

This Streamlit app allows you to analyze and visualize the stock prices of S&P 500 companies. You can filter companies by sector, download the filtered list, and plot the closing prices of selected stocks using real-time data from Yahoo Finance.

---

## Features

- **Sector Filtering:** Select one or more GICS sectors to filter S&P 500 companies.
- **Company List Download:** Download the filtered list of companies as a CSV file.
- **Stock Price Visualization:** Plot the closing prices (YTD) for up to 5 companies in the selected sector(s).
- **Interactive Sidebar:** Choose sectors and number of companies to visualize.

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository or download the code.**

2. **Install dependencies:**
   ```sh
   pip install streamlit pandas numpy matplotlib seaborn yfinance