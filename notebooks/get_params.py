#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:35:28 2018

@author: romeo
"""

import json

def get_param():
    """ get all parameters from a json file """
    credential_path = "C:\\Users\\rnd\\Desktop\\Formations_DS\\Quick_Demos_RND\\1_1_Demo_get_params\\"

    with open(credential_path+"params.json") as f:
        params = json.load(f)
    return params["host"], params["db_name"], params["login"], params["pw"]



host, db_name, login, pw = get_param()

