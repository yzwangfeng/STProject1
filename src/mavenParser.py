#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: Garfy
email: gaojianbo@pku.edu.cn
date: 2016-10-30
"""

from HTMLParser import HTMLParser

class mParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tbodyFlag = False
        self.tdNum = 0
        self.spanFlag = False
        self.mavenDict = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'tbody':
            self.tbodyFlag = True
        elif tag == 'td' and self.tbodyFlag:
            self.tdNum += 1
        elif tag == 'span' and self.tbodyFlag:
            self.spanFlag = True


    def handle_endtag(self, tag):
        if tag == 'span':
            self.spanFlag = False

    def handle_data(self, data):
        if self.tdNum == 2:
            self.mavenDict['classes'] = int(data)
        elif self.tdNum == 4:
            self.mavenDict['line1'] = data
        elif self.tdNum == 5 and self.spanFlag:
            self.mavenDict['line2'] = data
        elif self.tdNum == 7:
            self.mavenDict['branch1'] = data
        elif self.tdNum == 8 and self.spanFlag:
            self.mavenDict['branch2'] = data
        elif self.tdNum == 9 and not self.spanFlag:
            self.mavenDict['complexity'] = data
            self.tdNum += 1

    def get_result(self):
        return self.mavenDict
