import time
import requests
from prometheus_client import start_http_server, Gauge, generate_latest


# Define Prometheus metrics
# session_metric = Gauge('fiberhome_session', 'FiberHome session ID', ['device'])
uptime_metric = Gauge('fiberhome_uptime', 'FiberHome Uptime', ['device'])
cpu_usage_metric = Gauge('fiberhome_cpu_usage', 'FiberHome CPU usage', ['device'])
mem_total_metric = Gauge('fiberhome_mem_total', 'FiberHome total memory', ['device'])
mem_free_metric = Gauge('fiberhome_mem_free', 'FiberHome free memory', ['device'])
rxpower_metric = Gauge('fiberhome_rx_power', 'FiberHome optical rxpower', ['device'])
txpower_metric = Gauge('fiberhome_tx_power', 'FiberHome optical txpower', ['device'])
ponBytesSent_metric = Gauge('fiberhome_ponbytesent', 'FiberHome PON Byte Sent', ['device'])
ponBytesReceived_metric = Gauge('fiberhome_ponbytereceived', 'FiberHome PON Byte Received', ['device'])
ponPacketsSent_metric = Gauge('fiberhome_ponpacketssent', 'FiberHome PON Packet Sent ', ['device'])
ponPacketsReceived_metric = Gauge('fiberhome_ponpacketsreveived', 'FiberHome PON Packet Received', ['device'])
supplyvottage_metric = Gauge('fiberhome_supplyvottage', 'FiberHome PON supply voltage ', ['device'])
biascurrent_metric = Gauge('fiberhome_biascurrent', 'FiberHome PON bias Current', ['device'])
transceivertemperature_metric  = Gauge('fiberhome_transceivertemperature', 'FiberHome PON transceivertemperature', ['device'])


# FiberHome ONT device information
ONT_IP = '192.168.1.1'
ONT_USERNAME = 'user'
ONT_PASSWORD_HASH = '851AC19A19A523A64F361CEFD6908AAF'  # Replace with the actual password hash

def get_session():
    response = requests.get(f'http://{ONT_IP}/cgi-bin/ajax?ajaxmethod=get_refresh_sessionid', verify=False)
    return response.json().get('sessionid')

def login(session_id):
    data = {
        'username': ONT_USERNAME,
        'loginpd': ONT_PASSWORD_HASH,
        'port': 0,
        'sessionid': session_id,
        'ajaxmethod': 'do_login'
    }
    response = requests.post(f'http://{ONT_IP}/cgi-bin/ajax', data=data, verify=False)
    
    return response.json().get('session_valid')

def get_metrics(session_id):
    response = requests.get(f'http://{ONT_IP}/cgi-bin/ajax?ajaxmethod=get_base_info', verify=False)
    metrics = response.json()
    device = metrics['ModelName']
    uptime_metric.labels(device=device).set(metrics['uptime'])
    cpu_usage_metric.labels(device=device).set(metrics['cpu_usage'])
    mem_total_metric.labels(device=device).set(metrics['mem_total'])
    mem_free_metric.labels(device=device).set(metrics['mem_free'])
    rxpower_metric.labels(device=device).set(metrics['rxpower'])
    txpower_metric.labels(device=device).set(metrics['txpower'])
    ponBytesSent_metric.labels(device=device).set(metrics['ponBytesSent'])
    ponBytesReceived_metric.labels(device=device).set(metrics['ponBytesReceived'])
    ponPacketsSent_metric.labels(device=device).set(metrics['ponPacketsSent'])
    ponPacketsReceived_metric.labels(device=device).set(metrics['ponPacketsReceived'])
    supplyvottage_metric.labels(device=device).set(metrics['supplyvottage'])
    biascurrent_metric.labels(device=device).set(metrics['biascurrent'])
    transceivertemperature_metric.labels(device=device).set(metrics['transceivertemperature'])
    # Set values for more metrics here

def logout(session_id):
    data = {
        'sessionid': session_id,
        'username': 'common',
        'ajaxmethod': 'do_logout'
    }
    requests.post(f'http://{ONT_IP}/cgi-bin/ajax', data=data, verify=False)


if __name__ == '__main__':
    session_id = get_session()

    if session_id:
        start_http_server(8000)  # Start Prometheus exporter on port 8000
        print ("Starting at port :8080")
        try:
            logged_in_session_id = login(session_id)
            if logged_in_session_id:
                while True:
                    print ("Pulling metrics..")
                    get_metrics(logged_in_session_id)
                    time.sleep(30)  # Update metrics every 30 Seconds
        except KeyboardInterrupt:
            pass
        finally:
            logout(logged_in_session_id)
    else:
        print ("Cant reach ont.. ")

