#!/usr/bin/python

import json


def hsu(output_str=''):
    '''
    convert Huawei Server Upgrade Tool output to human-readable json
    '''
    output = json.loads(output_str)
    if output:
        if output['rc'] == 0:
            return output['data']
        else:
            return output['msg']
    
    return None


class FilterModule(object):
    '''
    custom jinja2 filters for handle HSU response
    '''

    def filters(self):
        return {
            'hsu': hsu
        }
