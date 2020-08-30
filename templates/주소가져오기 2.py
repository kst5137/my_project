import requests
import json
from tqdm import tqdm
import pandas as pd
url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"

req = requests.get(url)
json = req.json()
json

