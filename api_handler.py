import requests
import json
import logging
import pandas as pd
import os


logger = logging.getLogger(__name__)


class APIBMEHandler:
    
    def __init__(self, market):
        self.url_base = 'https://miax-gateway-jog4ew3z3q-ew.a.run.app'
        self.competi = 'mia_7'
        self.user_key = os.environ['API_KEY_MIAX']
        self.market = market

    def get_ticker_master(self):
        url = f'{self.url_base}/data/ticker_master'
        params = {'competi': self.competi,
                  'market': self.market,
                  'key': self.user_key}
        response = requests.get(url, params)
        tk_master = response.json()
        maestro_df = pd.DataFrame(tk_master['master'])
        return maestro_df

    def get_close_data_ticker(self, ticker):
        url = f'{self.url_base}/data/time_series'
        params = {'market': self.market,
                  'key': self.user_key,
                  'ticker': ticker}
        response = requests.get(url, params)
        tk_data = response.json()
        series_data = pd.read_json(tk_data, typ='series')
        return series_data

    def get_data_ticker(self, ticker):
        url = f'{self.url_base}/data/time_series'
        params = {'market': self.market,
                  'key': self.user_key,
                  'ticker': ticker,
                  'close': False}
        response = requests.get(url, params)
        tk_data = response.json()
        df_data = pd.read_json(tk_data, typ='frame')
        return df_data

