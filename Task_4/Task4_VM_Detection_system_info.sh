#!/bin/bash
# system_info.sh - Display system information

echo "===================================="
echo "       SYSTEM INFORMATION"
echo "===================================="
echo "Hostname: $(hostname)"
echo "Kernel Version:"
uname -r
echo "Current User:"
whoami
echo "Uptime:"
uptime -p
echo "CPU Info:"
lscpu | grep "Model name"
echo "Virtualization Detection:"
lscpu | grep "Virtualization"
echo "Hypervisor (if any):"
[ -f /proc/cpuinfo ] && grep -i "hypervisor" /proc/cpuinfo | head -1
echo "===================================="
