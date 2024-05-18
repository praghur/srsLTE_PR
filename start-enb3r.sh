#!/bin/bash
set -ux
tmux new-session -d -s enb3
tmux send-keys 'sudo srsenb /local/repository/etc/enb3.conf' C-m
tmux split-window -v
tmux select-layout even-vertical
tmux attach-session -d -t enb3
