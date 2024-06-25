#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:59:14 2024

@author: Joy
"""

def getBondDuration(y, face, couponRate, m, ppy=1):
        import numpy as np
        t=np.arange(1,ppy*m+1)
        cpn=couponRate*face
        df=1/(1+y/ppy)
        dft=[df**i for i in t]
        time=dft*t
        bondPrice=cpn*sum(dft)+dft[-1]*face
        timesum=cpn*sum(time)+dft[-1]*face*t[-1]
        bondDuration=timesum/bondPrice
        return(bondDuration)



# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1