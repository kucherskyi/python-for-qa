"""
Please figure out information from nginx access logs file - log.txt:
-all distinct requests' status codes
-resources users tried to access without permissions (HTTP status 403)
-created resources (HTTP status 201)
-requests count in time range 15:11:00 - 15:26:00
-successful requests rate (2xx / all count)
"""

import re
from datetime import datetime, time
from dateutil.parser import parse


def parse_log():

    li = []
    ip = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    time_request = r"[^[]*\[([^]]*)\]"
    url_reg = r'\"(.+?)\"'
    req_in_time = []
    with open('logs.txt', 'r') as log_file:
        for line in log_file.readlines():
            dic_reque = {}
            for elem in re.split(' ', line):
                if re.match(ip, elem):
                    dic_reque['ip'] = elem
            try:
                parsing = parse(re.match(time_request, line).groups()[0],
                                fuzzy=True)
                dic_reque['time'] = parsing
            except ValueError:
                dic_reque['time'] = 'none'

            try:
                reqest = re.findall(url_reg, line)
                try:
                    dic_reque['method'] = re.split(' ', reqest[0])[0]
                except ValueError:
                    dic_reque['method'] = 'UNIDENTIFIED'

                try:
                    dic_reque['url'] = reqest[1] + re.split(' ', reqest[0])[1]
                except:
                    dic_reque['url'] = "UNIDENTIFIED"

                try:
                    dic_reque['protocol'] = re.split(' ', reqest[0])[2]
                except:
                    dic_reque['protocol'] = "UNIDENTIFIED"

            except ValueError:
                pass

            try:
                dic_reque['status'] = re.findall("\s[0-9]+\s", line)[0].strip()
            except ValueError:
                dic_reque['status'] = 'UNIDENTIFIED'

            li.append(dic_reque)
    return li


def dist_status(parsed_logs):

    statuses = []
    for elem in parsed_logs:
        statuses.append(elem['status'])
    return 'All distinct requests status codes: \n{}'.format(statuses)


def permission_denide(parsed_logs):

    denied = []
    for elem in parsed_logs:
        if elem['status'] == '403':
            denied.append(elem['url'])
    return 'Access without permissions (status 403): \n{}'.format(denied)


def created(parsed_logs):

    creat = []
    for elem in parsed_logs:
        if elem['status'] == '201':
            creat.append(elem['url'])
    return 'Created resources : \n{}'.format(creat)


def req_in_time(parsed_logs):

    req_count = 0
    for elem in parsed_logs:
        if time(15, 11, 00) <= datetime.time(elem['time']) <= time(15, 26, 00):
            req_count += 1
    return'Requests count in time range 15:11:00 - 15:26:00 : {}'.format(req_count)


def rate(parsed_logs):

    valid = 0
    for elem in parsed_logs:
        if elem['status'].startswith('2') :
            valid += 1
    return 'Successful requests: {}%'.format(int((float(valid) /
                                                  len(parsed_logs)) * 100))


print dist_status(parse_log())
print permission_denide(parse_log())
print created(parse_log())
print req_in_time(parse_log())
print rate(parse_log())
