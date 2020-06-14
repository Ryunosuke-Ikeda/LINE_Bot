import datetime#######実験用
import numpy as np

def talk(res):

    if '自己紹介' in res:
        return '私は"Salieri"ただのボットです。白猫と三毛猫の判定ができます'

    if 'おはよう' in res:
        dt_now = datetime.datetime.now()
        return 'おはようございます。今日は{}年{}月{}日です。'.format(dt_now.year,dt_now.month,dt_now.day)
        
    if res=='Ver':
        return 'Salieri Ver 1.2.3'

    if res=='うるさい':
        return 'それな'
    else:
        return res





    


#print(talk('うるさい'))