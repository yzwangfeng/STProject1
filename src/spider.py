#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: Garfy
email: gaojianbo@pku.edu.cn
date: 2016-10-29
"""

import urllib2

class STSpider(object):
    """Spider for Software Testing"""
    def __init__(self, urlFilePath):
        self.urlFilePath = urlFilePath

    def reader(self):
        urlList = []
        urlFile = open(self.urlFilePath, "r")
        for url in urlFile.readlines():
            if not url:
                break
            else:
                urlList.append(url[:-1])
        return urlList

    def spider(self, url):
        req = urllib2.Request(url)
        fd = urllib2.urlopen(req)
        return fd.read()
