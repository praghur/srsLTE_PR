#!/bin/bash
set -ux
tmux new-session -d -s enb
tmux send-keys 'sudo srsenb /local/repository/etc/enb.conf' C-m
tmux split-window -v
tmux select-layout even-vertical
tmux attach-session -d -t enb
