#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  



s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)