#!/usr/bin/python
#
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: ibclient
author: "Nathan Gotz"
short_description: Manage Infoblox via Web API
description:
  - Manage Infoblox IPAM and DNS via Web API
"""

EXAMPLES = """

"""

RETURN = """

"""

from ansible.module_utils.basic import AnsibleModule

try:
    from ibclient.ibclient import IBClient
    HAS_IBCLIENT = True
except ImportError:
    HAS_IBCLIENT = False

try:
    import requests
    requests.packages.urllib3.disable_warnings()
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    """
    Ansible module to manage Infoblox operation by using REST API
    """
    module = AnsibleModule(
        argument_spec=dict(
            server=dict(required=True),
            username=dict(required=True),
            password=dict(required=True, no_log=True),
            action=dict(required=True, choices=[
                "get_memberservers", "get_dhcp_servers", "get_dhcpfailover",
                "get_network", "get_network_by_ip", "get_network_by_comment",
                "get_next_available_network",
                "get_next_available_address", "get_network_container",
                "get_range", "get_dns_record", "get_similar_dns_records",
                "get_fixedaddress", "get_fixedaddress_by_mac", "create_network",
                "create_network_container", "create_range", "create_reservedaddress",
                "create_fixedaddress", "create_ztp_fixedaddress", "create_a_record",
                "create_ptr_record", "create_dns_record", "update_network",
                "update_network_container", "update_reservedaddress",
                "update_fixedaddress_by_ip_addr",
                "update_fixedaddress_mac_addr", "delete_network",
                "delete_network_container", "delete_range",
                "delete_reservedaddress", "delete_fixedaddress",
                "delete_fixedaddress_by_mac", "delete_dns_records"
            ]),
            host=dict(required=False),
            network=dict(required=False),
            start_addr=dict(required=False),
            end_addr=dict(required=False),
            objref=dict(required=False),
            ip_address=dict(required=False),
            mac_address=dict(required=False),
            comment=dict(required=False),
            cidr=dict(required=False, type='raw'),
            num=dict(required=False, type='raw'),
            type=dict(required=False),
            record=dict(required=False),
            template=dict(required=False),
            exc_start=dict(required=False),
            exc_end=dict(required=False),
            options=dict(required=False),
            tftp_server=dict(required=False),
            cfg_file=dict(required=False),
            vendor_code=dict(required=False),
            fqdn=dict(required=False),
            api_version=dict(required=False, default="2.3.1"),
            dns_view=dict(required=False, default="default"),
            net_view=dict(required=False, default="default"),
            fields=dict(required=False, default=None, type='raw'),
        )
    )
    if not HAS_REQUESTS:
        module.fail_json(
            msg="Library 'requests' is required. Use 'sudo pip install requests' to fix it.")

    if not HAS_IBCLIENT:
        # This is a lie. ibclient (Infoblox client) is not on pypi (yet)
        module.fail_json(
            msg="Library 'ibclient' is required. Use 'sudo pip install ibclient' to fix it.")

    """
    Global vars
    """
    server = module.params["server"]
    username = module.params["username"]
    password = module.params["password"]
    action = module.params["action"]
    host = module.params["host"]
    network = module.params["network"]
    start_addr = module.params["start_addr"]
    end_addr = module.params["end_addr"]
    objref = module.params["objref"]
    ip_address = module.params["ip_address"]
    mac_address = module.params["mac_address"]
    comment = module.params["comment"]
    cidr = module.params["cidr"]
    num = module.params["num"]
    type = module.params["type"]
    record = module.params["record"]
    template = module.params["template"]
    exc_start = module.params["exc_start"]
    exc_end = module.params["exc_end"]
    options = module.params["options"]
    tftp_server = module.params["tftp_server"]
    cfg_file = module.params["cfg_file"]
    vendor_code = module.params["vendor_code"]
    fqdn = module.params["fqdn"]
    api_version = module.params["api_version"]
    dns_view = module.params["dns_view"]
    net_view = module.params["net_view"]
    fields = module.params["fields"]

    ib = IBClient(server, username, password, api_version, dns_view, net_view)

    if action == "get_memberservers":
        result = ib.get_memberservers()
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No member servers found"
            }
    elif action == "get_dhcp_servers":
        result = ib.get_dhcp_servers()
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No DHCP servers found"
            }
    elif action == "get_dhcpfailover":
        result = ib.get_dhcpfailover()
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No DHCP failover found"
            }
    elif action == "get_network":
        result = ib.get_network(network, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Network not found"
            }
    elif action == "get_network_by_ip":
        result = ib.get_network_by_ip(ip_address, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Network not found"
            }
    elif action == "get_network_by_comment":
        result = ib.get_network_by_comment(comment, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Network not found"
            }
    elif action == "get_next_available_network":
        result = ib.get_next_available_network(network, cidr, num)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No next available network"
            }
    elif action == "get_next_available_address":
        result = ib.get_next_available_network(network, num)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No next available IP address"
            }
    elif action == "get_network_container":
        result = ib.get_network_container(network, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Network Container not found"
            }
    elif action == "get_range":
        result = ib.get_range(start_addr, end_addr, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No DHCP Range"
            }
    elif action == "get_dns_record":
        result = ib.get_dns_record(type, record, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No DNS Record"
            }
    elif action == "get_similar_dns_records":
        result = ib.get_similar_dns_records(type, record, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "No Similar DNS Records"
            }
    elif action == "get_fixedaddress":
        result = ib.get_fixedaddress(ip_address, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Fixed Address not found"
            }
    elif action == "get_fixedaddress_by_mac":
        result = ib.get_fixedaddress_by_mac(mac_address, fields)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Fixed Address not found"
            }
    elif action == "create_network":
        result = ib.create_network(network, comment, template)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create network"
            }
    elif action == "create_network_container":
        result = ib.create_network_container(network, comment)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create network container"
            }
    elif action == "create_range":
        result = ib.create_range(network, start_addr, end_addr, exc_start,
                                 exc_end, options, template)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create DHCP range"
            }
    elif action == "create_reservedaddress":
        result = ib.create_reservedaddress(ip_address, host)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create reserved address"
            }
    elif action == "create_fixedaddress":
        result = ib.create_fixedaddress(ip_address, mac_address, host)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to fixed address"
            }
    elif action == "create_ztp_fixedaddress":
        result = ib.create_ztp_fixedaddress(ip_address, mac_addr, host, tftp_server, cfg_file, vendor_code)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to fixed address"
            }
    elif action == "create_a_record":
        result = ib.create_a_record(ip_address, fqdn)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create DNS A record"
            }
    elif action == "create_ptr_record":
        result = ib.create_ptr_record(ip_address, fqdn)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create DNS PTR record"
            }
    elif action == "create_dns_record":
        result = ib.create_dns_record(ip_address, fqdn)
        if result:
            result_json = {
                'changed': False,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to create DNS record"
            }
    elif action == "update_network":
        result = ib.update_network(network, comment)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to update network"
            }
    elif action == "update_network_container":
        result = ib.update_network_container(network, comment)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to update network container"
            }
    elif action == "update_reservedaddress":
        result = ib.update_reservedaddress(ip_address, host)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to update reserved address"
            }
    elif action == "update_fixedaddress_by_ip_addr":
        result = ib.update_fixedaddress_by_ip_addr(ip_address, mac_address, host)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to update fixed address"
            }
    elif action == "update_fixedaddress_mac_addr":
        result = ib.update_fixedaddress_by_mac_addr(mac_address, host)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to update fixed address"
            }
    elif action == "delete_network":
        result = ib.delete_network(network)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete network"
            }
    elif action == "delete_network_container":
        result = ib.delete_network_container(network)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete network container"
            }
    elif action == "delete_range":
        result = ib.delete_range(start_addr, end_addr)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete DHCP Range"
            }
    elif action == "delete_reservedaddress":
        result = ib.delete_reservedaddress(address)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete reserved address"
            }
    elif action == "delete_fixedaddress":
        result = ib.delete_fixedaddress(ip_address)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete fixed address"
            }
    elif action == "delete_fixedaddress_by_mac":
        result = ib.delete_fixedaddress_by_mac(mac_address)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete fixed address"
            }
    elif action == "delete_dns_records":
        result = ib.delete_dns_records(fqdn)
        if result:
            result_json = {
                'changed': True,
                'msg': result
            }
        else:
            result_json = {
                'msg': "Unable to delete DNS record"
            }
    module.exit_json(**result_json)

if __name__ == "__main__":
    main()
