import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from  urllib.request import Request, urlopen
import requests
import numpy as np
import config

def bytespdate2num(fmt,encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytes_converter(b):
        s=b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def graph_data(cn):
    apikey=config.pp_api_key

    print('Currently pulling:', cn)
    url='https://api.propublica.org/congress/v1/'+ cn +'/nominations.json'
    payload={'X-API-Key': apikey}
    source_code=requests.get(url,headers=payload)
    json=source_code.json()
    print(len(json['results'][0]['votes']))
    votes=json['results'][0]['votes']
    vote_data=[]
    for item in votes:
        vote_data.append(item['date'].replace('-','') + ',' +
                        str(item['total']['yes']) + ',' +
                        str(item['total']['no']) + ',' +
                        str(item['total']['not_voting']))

    print(vote_data)
    date,ty,tn,tnv = np.loadtxt(vote_data,delimiter=',',
                                unpack=True, converters={0: bytespdate2num('%Y%m%d')})
    print(date)
    plt.plot_date(date,ty, '-')
    plt.show()
congress_number = input('which version of Congress to plot(1-115): ')
graph_data(congress_number)
