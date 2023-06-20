from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .stock_analysis import getStockInfo, getOneStock
import json
# Create your views here.

def index(request):
    return render(request, "index.html")

stockData ={}
def list(request):
    stockList = ["MSFT", "NVDA", "AAPL", "GOOG", "AMZN", "NFLX", "AMD"]
    stockData = getStockInfo(stockList)
    return render(request, "list.html", {"stockData" : stockData})

def submit_form(request):
    if request.method == "POST":
        print(request.POST)
        ticker = request.POST.get("ticker")
        price = getOneStock(ticker)
        data = json.dumps(price)
        print(data)
        return render(request, "list.html", {"data": data, "stockData" : stockData})
    else :
        return render(request, "home.html")