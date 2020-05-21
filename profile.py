#!/usr/bin/env python
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN


tourDescription = """

# srsLTE Controlled RF

Use this profile to intantiate an end-to-end LTE network using simulated links
between eNB and UE (sending baseband IQ samples back and forth via ZMQ instead
of transmitting over the air via SDRs). Three d430 compute nodes will be
deployed (`epc`, `enb1`, and `rue1`), each with srsLTE 20.04.1, and connected to
the same LAN.

"""

tourInstructions = """

After your experiment becomes ready, login to `epc` via `ssh` and do the
following:

```
cd /local/repository
./start.sh
```

This will start a `tmux` session with two panes. The first one will be running
`srsepc`, while the second can be used to run tests with `ping` or `iperf`. If
you are not familiar with `tmux`, it's a terminal multiplexer that has some
similarities to screen. Here's a [tmux cheat sheet](https://tmuxcheatsheet.com),
but `ctrl-b o` (move to other pane) and `ctrl-b x` (kill pane), should get you
pretty far. `ctrl-b d` will detach you from the `tmux` session and leave it
running in the background. You can reattach with `tmux attach`.

After `srsepc` is running on `epc`, login to `enb1` and run the same commands
you did on `epc`. A `tmux` session will be created with `srsenb` running. You'll
see `srsepc` react to this as some handshaking occurs.

Finally, login to `rue1` and repeat the previous commands one last time. This
will start yet another `tmux` session with two panes. The first will be running
`srsue`, while the second can be used to run other commands. `srsue` will sync
with `srsenb` while using ZMQ to pass baseband IQ samples back and forth, as
opposed to sending them to an SDR for transmission over the air.

If you'd like to start everything manually, here are the commands:

```
# start srsepc (on epc node)
sudo srsepc /local/repository/etc/epc.conf

# start srsenb (on enb1 node)
sudo srsenb /local/repository/etc/enb.conf

# start srsue (on rue1 node)
sudo srsue /local/repository/etc/ue.conf
```

"""


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
# Add eNB node
enb1 = request.RawPC("enb1")
enb1.hardware_type = GLOBALS.HWTYPE
enb1.disk_image = GLOBALS.SRSLTE_IMG
iface2 = enb1.addInterface("eth1")
iface2.addAddress(rspec.IPv4Address("10.10.1.2", "255.255.255.0"))

# Add UE node
rue1 = request.RawPC("rue1")
rue1.hardware_type = GLOBALS.HWTYPE
rue1.disk_image = GLOBALS.SRSLTE_IMG
iface3 = rue1.addInterface("eth1")
iface3.addAddress(rspec.IPv4Address("10.10.1.3", "255.255.255.0"))

link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.link_multiplexing = True
link.vlan_tagging = True
link.best_effort = True

tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
