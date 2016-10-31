#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: Garfy
email: gaojianbo@pku.edu.cn
date: 2016-10-30

update:2016-10-31
"""

from spider import STSpider
from parser import STParser
from mavenParser import mParser
import json, time, os

resPath = os.path.abspath(os.path.join(os.getcwd(),os.path.dirname(__file__),"./../res/"))
projectsPath = os.path.abspath(os.path.join(os.getcwd(),os.path.dirname(__file__),"./../projects/"))
urlFilePath = os.path.join(resPath, "url.txt")
resultFilePath = os.path.join(resPath, "parser_result.json")
mavenResultFilePath = os.path.join(resPath, "result.json")


resultList = []
spider = STSpider(urlFilePath)
urlList = spider.reader()
for url in urlList:
    print url
    try:
        text = spider.spider(url)
        #print text
        parser = STParser(url)
        #print parser.aTypeDict
        parser.feed(text)
        parser.close()
        parserResult=parser.get_result()
        resultList.append(parserResult)
        time.sleep(5)
    except Exception, e:
        print e, url
        continue

jsonResult = json.dumps(resultList)
resultFile = open(resultFilePath, "w")
resultFile.write(jsonResult)
resultFile.close()




resultFile = open(resultFilePath, "r")
resultList = json.loads(resultFile.readline())
resultFile.close()

projectList = os.listdir(projectsPath)

mavenList = []
mavenDict = {}

for result in resultList:
    project = result['name']
    if project in projectList:
        mavenDict['name'] = result['name']
        mavenDict['watch'] = result['watchers']
        mavenDict['star'] = result['stargazers']
        mavenDict['fork'] = result['network']
        try:
            mavenPath = os.path.join(projectsPath, project, "target/site/cobertura/frame-summary.html")
            mavenFile = open(mavenPath, "r")
            mavenParser = mParser()
            mavenParser.feed(mavenFile.read())
            mavenFile.close()
            tmpDict = mavenParser.get_result()
        except Exception, e:
            print project
            print e
            continue

        mavenDict['classes'] = tmpDict['classes']
        mavenDict['line1'] = tmpDict['line1']
        mavenDict['line2'] = tmpDict['line2']
        mavenDict['branch1'] = tmpDict['branch1']
        mavenDict['branch2'] = tmpDict['branch2']
        mavenDict['complexity'] = tmpDict['complexity']

        mavenList.append(mavenDict)


resultFile = open(mavenResultFilePath, "w")
resultFile.write(json.dumps(mavenList))
resultFile.close()

print "[finish] %i Projects tested." % len(mavenList)






