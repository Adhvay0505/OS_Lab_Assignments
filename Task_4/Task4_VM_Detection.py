# detect_vm.py - Advanced Virtual Machine Detection

import os
import subprocess

def check_vm():
    indicators = 0
    evidence = []

    # 1. Check CPU info for hypervisor flags
    if os.path.exists("/proc/cpuinfo"):
        with open("/proc/cpuinfo", "r") as f:
            if "hypervisor" in f.read().lower():
                indicators += 1
                evidence.append("Hypervisor flag in /proc/cpuinfo")

    # 2. Check systemd detection
    try:
        result = subprocess.check_output("systemd-detect-virt", shell=True).decode().strip()
        if result != "none":
            indicators += 1
            evidence.append(f"systemd-detect-virt: {result}")
    except:
        pass

    # 3. Check common VM files
    vm_files = [
        "/.dockerenv",
        "/run/.containerenv",
        "/proc/vz",
        "/proc/xen",
        "/proc/scsi/scsi"
    ]
    for f in vm_files:
        if os.path.exists(f):
            indicators += 1
            evidence.append(f"Found VM file: {f}")

    # 4. Check manufacturer from DMI
    try:
        manuf = subprocess.check_output("cat /sys/class/dmi/id/product_name", shell=True).decode().strip()
        vm_keywords = ["Virtual", "VMware", "KVM", "QEMU", "VirtualBox", "Bochs"]
        if any(kw in manuf for kw in vm_keywords):
            indicators += 1
            evidence.append(f"Manufacturer: {manuf}")
    except:
        pass

    print("Virtual Machine Detection Result:")
    print("-" * 50)
    if indicators >= 2:
        print("High Likelyhood: This system is running inside a VIRTUAL MACHINE")
    elif indicators == 1:
        print("Possible: This might be a VM")
    else:
        print("Likely Physical Machine")
    
    print(f"\nEvidence found ({indicators}):")
    for e in evidence:
        print("  •", e)
    if not evidence:
        print("  None")

if __name__ == "__main__":
    check_vm()
