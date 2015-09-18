#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Based on drafted gist:
https://gist.github.com/joncasdam/cf6828726596110d1485

"""

import pandas as pd

if conversion_type == 'csv_to_excel':
	input_file = pd.read_csv(input_file)

	input_file.to_excel(output_file)
elif conversion_type == 'excel_to_csv';
	input_file = pd.read_excel(input_file)
	input_file.to_csv(outpu_file)