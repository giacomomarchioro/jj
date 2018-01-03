# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:59:53 2018
jj is module for writing scripts (e.g. for data analysis, learning how to use modules) interactivelly using the shell. 
You experiment using the shell, the command history is retrieved cleaned-up for invalid commands and eventually wrote 
in a .py file ready-to-go. 

It's light weight but for being so it assume this convention you have to import jj in this manner.

from jj import jj

if you do otherwise
@author: giacomo
"""

import readline 


class jj_c(object):
    '''
    This is the main class.
    '''
    
    def __init__(self):
        self.started = False
        self.start_signal = "jj.start()"
        
    def start(self):
        self.started = True
        
    def write(self,path = None ,filename = 'script.py'):
        historylines = []
        if self.started == True:
            i = 0
            looking_for_begining = True
            history_length = readline.get_current_history_length()
            while looking_for_begining:
                line = readline.get_history_item(history_length - i)
                if line == self.start_signal:
                    looking_for_begining = False
                else:
                    historylines.append(line)
                    i+=1
                

jj = jj_c()

