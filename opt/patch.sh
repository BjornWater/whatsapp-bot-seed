#!/usr/bin/env bash

# Patch for group messages error https://github.com/tgalal/yowsup/pull/1364
sed -i '106/:/ and not "-" in node["to"]:/'/home/bjorn/.local/lib/python2.7/site-packages/yowsup/layers/axolotl/layer.py
# no patches
