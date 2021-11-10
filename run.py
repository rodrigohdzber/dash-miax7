# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:56:43 2021

@author: Rodrigo
"""

from api_bme import APIBMEHandler
markets = ["DAX", "IBEX", "EUROSTOXX"]

ah = APIBMEHandler(market = "IBEX")


ticker_master = ah.get_ticker_master()
data = ah.get_close_data_ticker("SAN")


data.plot()