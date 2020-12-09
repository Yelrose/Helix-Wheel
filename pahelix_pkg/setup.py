import os
from setuptools import find_packages,setup

workdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(workdir, './requirements.txt')) as f:
    requirements = f.read().splitlines()


with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setup(
name = 'pahelixpackage',
author="fangxiaomin",
author_email="fangxiaomin01@baidu.com",
version = '0.1.3',
description = 'This version fixed the paddle requirement to be 2.0.0-rc0',
long_description = long_description,
long_description_content_type = "text/markdown",
packages = find_packages(),
url = "https://github.com/PaddlePaddle/PaddleHelix",
install_requires = requirements,
python_requires = '>=3.6',
)
