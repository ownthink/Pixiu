#!/usr/bin/env python
# -*- coding:utf-8 -*-
from distutils.core import setup

setup(name = 'jiagu',
    version = '0.01',
    description = 'Jiagu Natural Language Processing',
    author = 'Yener(Zheng Wenyu)',
    author_email = 'yener@ownthink.com',
    url = 'https://github.com/ownthink/Jiagu',
    install_requires=['tensorflow>=1.3.0', 'numpy>=1.12.1', 'pickle'],
    packages = ['jiagu'],
    package_dir = {"jiagu": "jiagu"},
	package_data={'jiagu':['*.*','model/*']}
    )
