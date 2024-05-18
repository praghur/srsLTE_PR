#!/usr/bin/env python
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN

class GLOBALS(object):
    UBUNTU_1804_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
    SRSLTE_IMG = "urn:publicid:IDN+emulab.net+image+PowderProfiles:U18LL-SRSLTE:2"
    HWTYPE = "d430"


pc = portal.Context()
request = pc.makeRequestRSpec()

# Add EPC node
epc = request.RawPC("epc")
epc.hardware_type = GLOBALS.HWTYPE
epc.disk_image = GLOBALS.SRSLTE_IMG
iface1 = epc.addInterface("eth1")
iface1.addAddress(rspec.IPv4Address("10.10.1.1", "255.255.255.0"))
iface1a = epc.addInterface("eth2")
iface1a.addAddress(rspec.IPv4Address("172.168.1.1", "255.255.255.0"))

# Add eNB1 node
enb1 = request.RawPC("enb1")
enb1.hardware_type = GLOBALS.HWTYPE
enb1.disk_image = GLOBALS.SRSLTE_IMG
iface2 = enb1.addInterface("eth1")
iface2.addAddress(rspec.IPv4Address("10.10.1.2", "255.255.255.0"))

# Add eNB2 node
enb2 = request.RawPC("enb2")
enb2.hardware_type = GLOBALS.HWTYPE
enb2.disk_image = GLOBALS.SRSLTE_IMG
iface4 = enb2.addInterface("eth1")
iface4.addAddress(rspec.IPv4Address("10.10.1.3", "255.255.255.0"))

# Add LL UE1 node
rue1 = request.RawPC("rue1")
rue1.hardware_type = GLOBALS.HWTYPE
rue1.disk_image = GLOBALS.SRSLTE_IMG
iface3 = rue1.addInterface("eth1")
iface3.addAddress(rspec.IPv4Address("10.10.1.4", "255.255.255.0"))

# Add LL UE2 node
rue2 = request.RawPC("rue2")
rue2.hardware_type = GLOBALS.HWTYPE
rue2.disk_image = GLOBALS.SRSLTE_IMG
iface5 = rue2.addInterface("eth1")
iface5.addAddress(rspec.IPv4Address("10.10.1.5", "255.255.255.0"))

# Add eNB3_Remote node
enb3r = request.RawPC("enb3r")
enb3r.hardware_type = GLOBALS.HWTYPE
enb3r.disk_image = GLOBALS.SRSLTE_IMG
iface6 = enb3r.addInterface("eth2")
iface6.addAddress(rspec.IPv4Address("172.168.1.2", "255.255.255.0"))

link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)
link.addInterface(iface5)
link.addInterface(iface6)

link.link_multiplexing = True
link.vlan_tagging = True
link.best_effort = True

tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
