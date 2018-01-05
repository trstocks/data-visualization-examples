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
    url='https://api.propublica.org/congress/v1/'+ cn +'/senate/members.json'
    payload={'X-API-Key': apikey}
    source_code=requests.get(url,headers=payload)
    json=source_code.json()
    print(len(json['results'][0]['members']))
    members=json['results'][0]['members']
    vote_data=[]
    for item in members:
        print(item['first_name'] + ' ' + item['last_name'])
        print('Total Votes: ' + str(item['total_votes']) + ' Missed Votes: ' + str(item['missed_votes']))

        vote_data.append(item['date_of_birth'].replace('-','') + ',' +
                        str(item['total_votes']) + ',' +
                         str(item['missed_votes']))
    print(vote_data)
    dob,tvotes,mvotes = np.loadtxt(vote_data,delimiter=',',
                                unpack=True, converters={0: bytespdate2num('%Y%m%d')})
    print(dob)
    plt.plot_date(dob,mvotes, '-')
    plt.show()
congress_number = input('which version of Congress to plot(1-115): ')
graph_data(congress_number)
