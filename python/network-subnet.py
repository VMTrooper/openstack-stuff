import os
import logging
from neutronclient.neutron import client
logging.basicConfig(level=logging.DEBUG)
neutron = client.Client('2.0', username=os.environ['OS_USERNAME'], password=os.environ['OS_PASSWORD'], tenant_name=os.environ['OS_TENANT_NAME'], auth_url=os.environ['OS_AUTH_URL'], ca_cert=os.environ['OS_CACERT'])
#Get the subnet ID that you need
#print "".join(neutron.list_subnets())

req = {"subnet": {"allocation_pools": [{"start": "10.115.97.1", "end": "10.115.97.100"}, {"start": "10.115.97.254", "end": "10.115.97.254"}]}}

neutron.update_subnet("bfa0aeef-0314-438c-a405-113d00f21894", req)