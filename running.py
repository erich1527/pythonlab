#!/usr/bin/env python3.7

from os import getenv

stage = getenv("STAGE", default="dev").upper()
output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)