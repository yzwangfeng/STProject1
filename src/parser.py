#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: Garfy
email: gaojianbo@pku.edu.cn
date: 2016-10-29
"""

from HTMLParser import HTMLParser

class STParser(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.flag = False
        urlTail = url[18:]+'/'
        aTypeList = [
            "watchers",
            "stargazers",
            "network"]
        self.aTypeDict = {}
        for aType in aTypeList:
            self.aTypeDict[urlTail+aType] = aType
        self.resultDict = {}
        self.resultKey = ""
        self.resultDict['name'] = url.split('/')[-1]

    def handle_starttag(self, tag, attrs):
        if tag=="a" and attrs:
            for key, value in attrs:
                if key=="href" and self.aTypeDict.has_key(value):
                    self.flag = True
                    self.resultKey = self.aTypeDict[value]

    def handle_endtag(self, tag):
        self.flag = False

    def handle_data(self, data):
        if self.flag:
            self.resultDict[self.resultKey] = int(data.replace(',', ''))

    def get_result(self):
        return self.resultDict


