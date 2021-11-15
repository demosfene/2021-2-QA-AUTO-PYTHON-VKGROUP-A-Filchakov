import os

FILENAME = os.path.join(os.path.dirname(__file__), "access.log")


def get_data():
    connections = []
    results = {}
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.split()
            current_connection = {
                'ip': line[0],
                'date': line[3][1:],
                'type': line[5][1:],
                'url': line[6],
                'status_code': line[8],
                'length': line[9]
            }
            connections.append(current_connection)
    results['total_connections'] = len(connections)

    results['count_by_types'] = {}
    for conn_type in ["POST", "GET", "HEAD", "UPDATE", "DELETE", "PUT", "PATCH", "TRACE", "CONNECT", "OPTIONS"]:
        count = len([x for x in connections if x['type'] == conn_type])

        if count:
            results['count_by_types'][conn_type] = count

    urls = {}
    results['top_by_urls'] = {}
    for connection in connections:
        urls.setdefault(connection["url"], 0)
        urls[connection["url"]] += 1

    for idx, url in enumerate({k: v for k, v in sorted(urls.items(), key=lambda item: item[1], reverse=True)}):
        results['top_by_urls'][url] = urls[url]
        if idx > 8:
            break

    results['top_by_length_4xx'] = {}
    only_4xx_errors = [x for x in connections if x['status_code'].startswith('4')]
    only_4xx_errors = sorted(only_4xx_errors, key=lambda item: int(item['length']), reverse=True)
    for elem in only_4xx_errors[:5]:
        results['top_by_length_4xx'][elem['url']] = {'status_code': elem['status_code'],
                                                     'length': elem['length'],
                                                     'ip': elem['ip']
                                                     }

    results['top_by_conn_count_5xx'] = {}
    only_5xx_errors = [x for x in connections if x['status_code'].startswith('5')]
    users_ips = {}
    for only_5xx_error in only_5xx_errors:
        users_ips.setdefault(only_5xx_error["ip"], 0)
        users_ips[only_5xx_error["ip"]] += 1

    for idx, ip in enumerate({k: v for k, v in sorted(users_ips.items(), key=lambda item: item[1], reverse=True)}):
        results['top_by_conn_count_5xx'][ip] = {'count': users_ips[ip]}
        if idx > 3:
            break

    return results
