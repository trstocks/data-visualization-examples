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

def graph_data(sn):
    fig= plt.figure()
    ax1=plt.subplot2grid((1,1), (0,0))
    plt.ylabel('Price')
    plt.xlabel('Date')
    apikey=config.aa_api_key
    print('Currently pulling:', sn)
    url='https://www.alphavantage.co/query'
    function='TIME_SERIES_daily'
    symbol=sn
    outputsize='full'
    payload={'apikey': apikey,'function':function,'symbol':symbol,'outputsize':outputsize}
    source_code=requests.get(url,params=payload)
    json=source_code.json()
    #print(len(json()))
    stock=json['Time Series (Daily)']
    stock_data=[]
    for item in stock:
        collect_data=''
        print(item)
        print(stock[item])
        for data in stock[item]:
            #print(stock[item][data])
            collect_data+=str(stock[item][data]) + ','
        collect_data=collect_data.split(',')
        collect_data.pop()
        if '16:00:00' in item:
            collect_data.insert(0,item.replace(' 16:00:00',''))
        else:
            collect_data.insert(0,item)
        print(collect_data)

        stock_data.append(str(collect_data[0]+','+collect_data[1]+','+collect_data[2]+','+
                        collect_data[3]+','+collect_data[4]+','+collect_data[5]))

    date,openp,highp,lowp,closep,volume = np.loadtxt(stock_data,delimiter=',',
                                unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
    ax1.plot_date(date,closep, '-')
    #ax1.fill_between(date,closep, 83.5, alpha=.5,edgecolor='k')
    ax1.grid(True)#, color = 'g', linestyle='-',linewidth=3)

    ax1.yaxis.label.set_color('m')
    ax1.xaxis.label.set_color('c')
    ax1.set_yticks([83.5,84,84.5])


    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.subplots_adjust(left=.09,bottom=.16,right=.94, top=.95, wspace=.2,hspace=.2)
    plt.show()
stock_name = input('which stock name(i.e. tsla)): ')
graph_data(stock_name)
