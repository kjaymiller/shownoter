import requests
import pytest

## Connects to the internet browser and travels to Shownoter

request = requests.get('localhost:5000')
assert request.ok

## 
