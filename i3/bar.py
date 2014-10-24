# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
                format="%a %-d %b %X",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
                format="♪{volume}",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")
status.register("mem",
                format="{used_mem} [{percent_used_mem}%]")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
                format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via dbus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
status.register("battery",
                format="{status}/{consumption:.2f}W {percentage:.2f}% [{percentage_design:.2f}%] {remaining:%E%hh:%Mm}",
                alert=True,
                alert_percentage=5,
                status={
                    "DIS": "↓",
                    "CHR": "↑",
                    "FULL": "=",
                },)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
                path="/home",
                format="{used}/{total}G [{percentage_used}%]",)
status.run()
