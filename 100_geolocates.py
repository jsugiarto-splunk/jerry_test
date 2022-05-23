"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import random
import socket
import struct
import time

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'geolocate_ip_1' block
    geolocate_ip_1(container=container)

    return

def geolocate_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_1() called')

    # collect data for 'geolocate_ip_1' call

    parameters = []
    for i in range(25):
        parameters.append({
            'ip': socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),
        })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_1", callback=geolocate_ip_2)

    return

def geolocate_ip_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_2() called')
    
    parameters = []
    for i in range(25):
        parameters.append({
            'ip': socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),
        })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_2", callback=geolocate_ip_3)

    return

def geolocate_ip_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_3() called')
    
    parameters = []
    for i in range(25):
        parameters.append({
            'ip': socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),
        })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_2", callback=geolocate_ip_4)

    return

def geolocate_ip_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_4() called')

    parameters = []
    for i in range(25):
        parameters.append({
            'ip': socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),
        })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_4", parent_action=action)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    time.sleep(120)
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return