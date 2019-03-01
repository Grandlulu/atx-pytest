# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: WEditor
# pip install --pre --upgrade weditor

import os

filePath = os.path.dirname(os.path.abspath("__file__"))
venvPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "venv", "Scripts")

print(venvPath)
os.system(venvPath + "\\python -m weditor")