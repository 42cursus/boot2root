#!/usr/bin/env python
"""Turn a shell with effective UID 0 into one with real and effective UID 0."""

import os

if os.geteuid() != 0:
    raise SystemExit("This step requires effective UID 0.")
os.setgroups([0])
os.setgid(0)
os.setuid(0)
os.execl("/bin/sh", "sh")
