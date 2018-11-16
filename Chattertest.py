# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:12:27 2018

@author: suryaprakash.rao
"""

import chatterbot
import string


bot=chatterbot.ChatBot('ibot',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
bot.train('chatterbot.corpus.english')

while True:
     qus=input('You: ')
     
     if qus=='N':
         break
     ans=bot.get_response(qus)
     print('Bot: ',ans)