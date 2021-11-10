# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:56:43 2021

@author: Rodrigo
"""

from api_bme import APIBMEHandler

ah = APIBMEHandler(market = "IBEX")

santander = ah.get_close_data_ticker("SAN")

ticker_master = ah.get_ticker_master()
santander.plot()