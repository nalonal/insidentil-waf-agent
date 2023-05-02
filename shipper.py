import time, json, tailer,datetime,re
from elasticsearch import Elasticsearch

def ship_logs(log_file, es_host, es_port, index_name):
    username = 'elastic'
    password = 'mysecretpassword'
    es = Elasticsearch(f"http://{es_host}:{es_port}", verify_certs=False, basic_auth=(username, password))
    for line in tailer.follow(open(log_file)):
        line = line.strip()
        parsed_json = json.loads(line)
        parsed_json = parsed_json['transaction']
        new_json = {}
        for key, value in parsed_json.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    new_key = key + "." + sub_key
                    new_json[new_key] = sub_value
            else:
                new_json[key] = value
        time_stamp = parsed_json['time_stamp']
        # convert string to datetime object
        dt_obj = datetime.datetime.strptime(time_stamp, "%a %b %d %H:%M:%S %Y")
        # format datetime object to Elasticsearch timestamp
        es_timestamp = dt_obj.strftime("%Y-%m-%dT%H:%M:%S.%fZ")        
        new_json['timestamp_crawl'] = es_timestamp

        output_json = json.dumps(new_json)
        es.index(index=index_name, document=output_json)

ship_logs("modsec/modsec_audit.log", "localhost", 9200, "modsec")