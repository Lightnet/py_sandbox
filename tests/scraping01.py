#https://www.youtube.com/watch?v=DqtlR0y0suo

import requests
import pandas as pd

def main():
  url = ""
  querystring = {"api","TEST"}
  payload = ""
  headers = {}

  respone = requests.request("GET", url, data=payload, headers=headers,params=querystring)
  print(respone.text)
  print(respone.json())
  data = respone.json()
  print(data["api"])


if __name__ == '__main__':
  main()