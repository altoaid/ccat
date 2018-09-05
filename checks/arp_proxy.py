# ARP-proxy options check
# Input:
#        interface dictionary
#        interface type from vlanmap
# Output:
#        result dictionary
#           {'ARP-proxy': {'ARP-proxy': [severity(int), 'message', 'best practice']}
#

def global_check(global_dct):
    if 'arp_proxy' in global_dct:
        if global_dct['arp_proxy']=='disable':
            return 1,{'ARP-proxy': {'ARP-proxy': [2,'DISABLED']}}
    else:
        return 0, {'ARP-proxy': {'ARP-proxy': [0, 'enabled','ghj']}}
    return 0, 0


def _iface_check__proxy_check(iface_dct,result,scale):
    if 'arp_proxy' in iface_dct:
        if iface_dct['arp_proxy']=='no':
            return {'ARP-proxy':[scale[1],'ENABLED']}
    else:
        return {'ARP-proxy': [scale[0], 'DISABLED','ARP-proxy should be disabled']}




def iface_check(iface_dct, vlanmap_type):
    result = {}

    # If this network segment is TRUSTED - enabled cdp is not a red type of threat, it will be colored in orange
    if vlanmap_type == 'TRUSTED':
        return _iface_check__proxy_check(iface_dct,  result, [1, 2])

    # Otherwise if network segment is CRITICAL or UNKNOWN or vlanmap is not defined - enabled cdp is a red type of threat
    else:
        return _iface_check__proxy_check(iface_dct,  result, [0, 2])





