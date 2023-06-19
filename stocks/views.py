from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .stock_analysis import getStockInfo
# Create your views here.

def index(request):
    return HttpResponse("hello, world. you're at the polls index")

def list(request):
    stockList = ["MSFT", "NVDA", "AAPL", "GOOG", "AMZN", "NFLX", "AMD"]
    stockData = getStockInfo(stockList)
    return render(request, "list.html", {"stockData" : stockData})