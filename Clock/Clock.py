#1.1
from datetime import datetime
import pytz
from os import system
from time import sleep
from cursor import hide


Berlin=pytz.timezone('Europe/Berlin')
London=pytz.timezone('Europe/London')
Moscow=pytz.timezone('Europe/Moscow')
Sydney=pytz.timezone('Australia/Canberra')
Washington=pytz.timezone('US/Eastern')
LosAngeles=pytz.timezone('America/Los_Angeles')
NewDelhi=pytz.timezone('Asia/Calcutta')
NewYork=pytz.timezone('America/New_York')
Brussels=pytz.timezone('Europe/Brussels')
Paris=pytz.timezone('Europe/Paris')
Tokyo=pytz.timezone('Asia/Tokyo')
MexicoCity=pytz.timezone('America/Mexico_City')


x=True
while x == True:
    hide()
    datetime_Berlin=datetime.now(Berlin)
    datetime_London=datetime.now(London)
    datetime_Moscow=datetime.now(Moscow)
    datetime_Sydney=datetime.now(Sydney)
    datetime_Washington=datetime.now(Washington)
    datetime_LosAngeles=datetime.now(LosAngeles)
    datetime_NewDelhi=datetime.now(NewDelhi)
    datetime_NewYork=datetime.now(NewYork)
    datetime_Brussels=datetime.now(Brussels)
    datetime_Paris=datetime.now(Paris)
    datetime_Tokyo=datetime.now(Tokyo)
    datetime_MexicoCity=datetime.now(MexicoCity)

    print('Los Angeles time:     ', datetime_LosAngeles.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Mexico City time:     ', datetime_MexicoCity.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Washington D.C. time: ', datetime_Washington.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('New York time:        ', datetime_NewYork.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('London time:          ', datetime_London.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Berlin time:          ', datetime_Berlin.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Brussels time:        ', datetime_Brussels.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Paris time:           ', datetime_Paris.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Moscow time:          ', datetime_Moscow.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('New Delhi time:       ', datetime_NewDelhi.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Tokyo time:           ', datetime_Tokyo.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    print('Sydney time:          ', datetime_Sydney.strftime('%b.%d.%Y - %H:%M:%S --> GMT%z'))
    sleep(1)
    system('cls')
