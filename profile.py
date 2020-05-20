#!/usr/bin/env python
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN


tourDescription = """

# srsLTE Controlled RF

Use this profile to intantiate and end-to-end LTE network in a controlled RF
environment (SDRs with wired connections) using srsLTE release 20.04.1.

The following nodes will be deployed:

* Intel NUC5300/B210 w/ srsLTE (`rue1`)
* Intel NUC5300/B210 w/ srsLTE (`enb1`)

"""

tourInstructions = """

After your experiment becomes ready, login to the `enb1` via `ssh` and do the
following:

```
cd /local/repository
./start.sh
```

This will start a `tmux` session with three panes, running `srsepc` and
`srsenb`, and then leaving your cursor in the last pane. After you've associated
a UE with this eNB, you can use the third pane to run tests with `ping` or
`iperf`. If you are not familiar with `tmux`, it's a terminal multiplexer that
has some similarities to screen. Here's a [tmux cheat
sheet](https://tmuxcheatsheet.com), but `ctrl-b o` (move to other pane) and
`ctrl-b x` (kill pane), should get you pretty far. `ctrl-b d` will detach you
from the `tmux` session and leave it running in the background. You can reattach
with `tmux attach`.

If you'd like to start `srsepc` and `srsenb` manually, here are the commands:

```
# start srsepc
sudo srsepc /etc/srslte/epc.conf

# start srsenb
sudo srsenb /etc/srslte/enb.conf
```

After `srsepc` and `srsenb` have started, login to `rue1` and do:

```
cd /local/repository
./start.sh
```

This will start a `tmux` session with two panes: one running srsue and the other
holding a spare terminal for running tests with `ping` and `iperf`. Again, if
you'd like to run `srsue` manually, do:

```
sudo srsue /etc/srslte/ue.conf
```

"""


class GLOBALS(object):
    UBUNTU_1804_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
    SRSLTE_IMG = "urn:publicid:IDN+emulab.net+image+PowderProfiles:U18LL-SRSLTE:1"
    HWTYPE = "d430"


pc = portal.Context()
request = pc.makeRequestRSpec()

# Add EPC node
epc = request.RawPC("epc")
epc.hardware_type = GLOBALS.HWTYPE
epc.disk_image = GLOBALS.SRSLTE_IMG

# Add eNB node
enb1 = request.RawPC("enb1")
enb1.hardware_type = GLOBALS.HWTYPE
enb1.disk_image = GLOBALS.SRSLTE_IMG

# Add UE node
rue1 = request.RawPC("rue1")
rue1.hardware_type = GLOBALS.HWTYPE
rue1.disk_image = GLOBALS.SRSLTE_IMG

link = request.Link("lan")
link.addNode(epc)
link.addNode(enb1)
link.addNode(rue1)
link.link_multiplexing = True
link.vlan_tagging = True
link.best_effort = True

tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
