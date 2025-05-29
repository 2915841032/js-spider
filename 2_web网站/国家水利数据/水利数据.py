# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# Copyright (c) 2024 愤怒的it男, All Rights Reserved.
# FileName : code.py
# Date     : 2024.03.05
# Author   : 愤怒的it男
# Version  : 1.0.0
# Node     : 欢迎关注微信公众号【愤怒的it男】
#
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import csv
import requests
from datetime import datetime, timedelta


def getMonitorWellWithExtranet():
    url = 'https://geocloud.cgs.gov.cn/api/geocloud/v1/open-api/call'
    data = {
        "apiCode": "getMonitorWellWithExtranet",
        "header": {
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJnZW9jbG91ZCIsImV4cCI6MTcxNDk0OTY0Nn0.sdF35DlUWwa_2CUvgrkiytO_-LlAPandGdnIZJfAOvg"
        }
    }
    response = requests.post(url,  json=data)

    return response.json()


def getMonitorWellISiteInfoWithExtanet(id):
    url = 'https://geocloud.cgs.gov.cn/api/geocloud/v1/open-api/call'
    data = {
        "apiCode": "getMonitorWellISiteInfoWithExtanet",
        "data": {
            "id": id,
            "prefixTopic": ""
        },
        "header": {
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJnZW9jbG91ZCIsImV4cCI6MTcxNDk0OTY0Nn0.sdF35DlUWwa_2CUvgrkiytO_-LlAPandGdnIZJfAOvg"
        }
    }
    response = requests.post(url=url, json=data)
    print('getMonitorWellISiteInfoWithExtanet:' + str(response.status_code))
    return response.json()


def getMonitorWellLineDataWithExtranet(id):
    url = 'https://geocloud.cgs.gov.cn/api/geocloud/v1/open-api/call'
    data = {
        "apiCode": "getMonitorWellLineDataWithExtranet",
        "data": {
            "id": id,
            "beginTime": "2024-02-20",
            "endTime": "2024-03-06",
            "prefixTopic": ""
        },
        "header": {
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJnZW9jbG91ZCIsImV4cCI6MTcxNDk0OTY0Nn0.sdF35DlUWwa_2CUvgrkiytO_-LlAPandGdnIZJfAOvg"
        }
    }
    response = requests.post(url=url, json=data)
    print('getMonitorWellLineDataWithExtranet:' + str(response.status_code))
    return response.json()


def main():
    monitorWellWithExtranet = getMonitorWellWithExtranet()
    print(monitorWellWithExtranet)
    start_date = datetime(2024, 2, 25, 0, 0, 0)
    end_date = datetime(2024, 3, 1, 0, 0, 0)
    date_list = []
    while start_date < end_date:
        date_list.append(start_date.strftime('%Y-%m-%d %H:%M:%S'))
        start_date += timedelta(hours=1)

    with open('全国地下水动态监测数据2.csv', 'a', encoding='utf-8', newline='') as file:
        error_features = []
        for i, feature in enumerate(monitorWellWithExtranet['features']):
            data = {}
            data['WELL_DBK'] = feature['properties']['WELL_DBK']
            data['LONGITUDE'] = feature['geometry']['coordinates'][0]
            data['LATITUDE'] = feature['geometry']['coordinates'][1]
            monitorWellISiteInfoWithExtanet = getMonitorWellISiteInfoWithExtanet(data['WELL_DBK'])
            if monitorWellISiteInfoWithExtanet['data'] is None:
                error_features.append(feature)
                print(error_features)
                continue
            else:
                data.update(monitorWellISiteInfoWithExtanet['data'][0])
            monitorWellLineDataWithExtranet = getMonitorWellLineDataWithExtranet(data['WELL_DBK'])
            if monitorWellLineDataWithExtranet['data'] is None:
                error_features.append(feature)
                print(error_features)
                continue
            else:
                for t in date_list:
                    data['sw({})'.format(t)] = ''
                    data['ms({})'.format(t)] = ''
                for m in monitorWellLineDataWithExtranet['data']:
                    monitor_time = m['monitor_time'][:13] + ':00:00'
                    data['sw({})'.format(monitor_time)] = m['sw']
                    data['ms({})'.format(monitor_time)] = m['ms']
                print('正在采集第{}个监测点的数据……'.format(i + 1))
                if i == 0:
                    fieldnames = list(data.keys())
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                writer.writerow(data)
        print(error_features)


if __name__ == "__main__":
    main()