# -*- coding: utf-8 -*-
"""
Write some functions to asses the forecast quality 
that takes actuals and forecasts, a list of floats, 
and returns the error measures, 
MSE, RMSE, MAPE.

Indication: you can use locals() or globals() 
to call a function from a string
that is located in this object
e.g. function_x(var1,var2) 
locals()["function_x"](var1,var2)
globals()["function_x"](var1,var2)

"""

import numpy as np


def mse(actuals, forecasts):
    metric = ((actuals - forecasts) ** 2).mean()
    return metric


def rmse(actuals, forecasts):
    metric = np.sqrt(actuals, forecasts)
    return metric


def mape(actuals, forecasts):
    metric = (np.abs(actuals - forecasts) / actuals).mean() * 100
    return metric
