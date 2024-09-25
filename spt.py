
import yfinance as yf
# Defining portfolios for product-based and service-based companies
product_portfolio = {
    'AAPL': {'shares': 10, 'buy_price': 150.00},  # Apple stock
    'TSLA': {'shares': 5, 'buy_price': 700.00},   # Tesla stock
    'MSFT': {'shares': 8, 'buy_price': 250.00},   # Microsoft stock
}

service_portfolio = {
    'RELIANCE.BO': {'shares': 20, 'buy_price': 2400.00},  # Reliance Industries stock
    'TCS.BO': {'shares': 10, 'buy_price': 3300.00},       # TCS stock
    'HDFCBANK.BO': {'shares': 15, 'buy_price': 1500.00},  # HDFC Bank stock
    'INFY.BO': {'shares': 12, 'buy_price': 1700.00},      # Infosys stock
    'WIPRO.NS': {'shares': 20, 'buy_price': 2400.00},     # Wipro stock
    'SBIN.BO': {'shares': 25, 'buy_price': 500.00},       # State Bank of India stock
}

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period='1d')
    current_price = stock_info['Close'].iloc[-1]
    return current_price

def calculate_portfolio_value(portfolio, title):
    total_value = 0
    print(f"\n{title}")
    print(f"{'Stock':<15}{'Shares':<10}{'Buy Price':<15}{'Current Price':<15}{'Value':<15}")
    print("="*70)
    
    for stock, info in portfolio.items():
        current_price = get_stock_data(stock)
        stock_value = info['shares'] * current_price
        total_value += stock_value
        print(f"{stock:<15}{info['shares']:<10}{info['buy_price']:<15}{current_price:<15.2f}{stock_value:<15.2f}")
    
    print("="*70)
    print(f"Total {title} Value: ₹{total_value:.2f}")
    return total_value

def track_portfolio():
    # Calculating  displaying values for both portfolios
    calculate_portfolio_value(product_portfolio, 'Product Based Companies')
    calculate_portfolio_value(service_portfolio, 'Service Based Companies')

# Track the portfolio
track_portfolio()