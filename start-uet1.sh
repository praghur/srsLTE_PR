#!/bin/bash
set -ux
tmux new-session -d -s uet1
tmux send-keys 'sudo srsue /local/repository/etc/uet1.conf' C-m
tmux split-window -v
tmux select-layout even-vertical
tmux attach-session -d -t uet1
