# caption - Manage markdown captions
#
# Copyright (c) 2020 flywire
# forked from yafg - https://git.sr.ht/~ferruck/yafg
# Copyright (c) 2019 Philipp Trommler
#
# SPDX-License-Identifier: GPL-3.0-or-later
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree import ElementTree

class captionTreeprocessor(Treeprocessor):
    def __init__(
        self,
        md,
        captionPrefix,
        captionNumbering,
        captionPrefixClass,
        captionClass,
        contentClass,
        stripTitle):
        self.md = md
        self.captionPrefix = captionPrefix
        self.captionNumbering = captionNumbering
        self.captionNumber = 0
        self.captionPrefixClass = captionPrefixClass
        self.captionClass = captionClass
        self.contentClass = contentClass
        self.stripTitle = stripTitle

    def buildContentElement(self, par):
        attrib = par.attrib
        par.clear()
        par.tag = "figure"
        for k, v in attrib.items():
            par.set(k, v)
        if self.contentClass is not "":
            par.set("class", self.contentClass)
        par.set("id", "_caption-{}".format(self.captionNumber))
        par.text = "\n"
        par.tail = "\n"

    def buildCaptionElement(self, par, title):
        caption = ElementTree.SubElement(par, "figcaption")
        if self.captionClass is not "":
            caption.set("class", self.captionClass)
        if self.captionNumbering:
            captionPrefixSpan = ElementTree.SubElement(caption, "span")
            captionPrefixSpan.text = "{}&nbsp;{}:".format(self.captionPrefix, self.captionNumber)
            captionPrefixSpan.tail = " {}".format(title)
            if self.captionPrefixClass is not "":
                self.captionPrefix.set("class", self.captionPrefixClass)
        else:
            caption.text = title
        caption.tail = "\n"

    def run(self, root):
        for par in root.findall("./p[img]"):
            img = par.find("img")
            self.captionNumber += 1
            self.buildContentElement(par)
            img.tail = "\n"
            par.append(img)
            self.buildCaptionElement(par, img.get("title"))
            if self.stripTitle:
                del img.attrib["title"]

class captionExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            "captionPrefix" : ["Figure", "The text to show in front of the image caption."],
            "captionNumbering" : [False, "Add the caption number to the prefix."],
            "captionPrefixClass" : ["", "CSS class to add to the caption prefix <span /> element."],
            "captionClass" : ["", "CSS class to add to the caption element."],
            "contentClass" : ["", "CSS class to add to the content element."],
            "stripTitle" : [False, "Strip the title from the <img />."],
        }
        super(captionExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.treeprocessors.register(
            captionTreeprocessor(
                md,
                captionPrefix=self.getConfig("captionPrefix"),
                captionNumbering=self.getConfig("captionNumbering"),
                captionPrefixClass=self.getConfig("captionPrefixClass"),
                captionClass=self.getConfig("captionClass"),
                contentClass=self.getConfig("contentClass"),
                stripTitle=self.getConfig("stripTitle"),
            ),
            "captiontreeprocessor",
            8)

def makeExtension(**kwargs):
    return captionExtension(**kwargs)