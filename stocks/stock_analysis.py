import yfinance as yf
import pandas as pd

stockList = ["MSFT", "NVDA", "AAPL", "GOOG", "AMZN", "NFLX", "AMD"]

def getStockInfo(list):
  stockData = {}
  for stockSymbol in list:
      stock = yf.Ticker(stockSymbol)
      stockInfo = stock.info

      currentPrice = stockInfo["currentPrice"]
      previousClose = stockInfo["regularMarketPreviousClose"]
      percentageIncrease = ((currentPrice - previousClose) / previousClose) * 100

      stockData[stockSymbol] = {
          "currentPrice": currentPrice,
          "percentageIncrease": round(percentageIncrease,2)
      }

  return stockData

def getOneStock(ticker):
   
   ticker = yf.Ticker(ticker)
   tickerInfo = ticker.info
   currentPrice = tickerInfo["currentPrice"]
   previousClose = tickerInfo["regularMarketPreviousClose"]
   percentageIncrease = ((currentPrice - previousClose) / previousClose) * 100
   tickerData = {
      "currentPrice": currentPrice,
      "percentageIncrease": round(percentageIncrease,2)
   }
   return tickerData
