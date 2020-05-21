#!/bin/bash
set -ux
tmux new-session -d -s epc
tmux send-keys 'sudo srsepc /local/repository/etc/epc.conf' C-m
tmux split-window -v
tmux select-layout even-vertical
tmux attach-session -d -t epc
