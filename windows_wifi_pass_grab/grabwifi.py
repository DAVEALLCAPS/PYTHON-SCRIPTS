import subprocess

subprocess.check_call(["netsh", "wlan", "show", "profiles"])
