﻿#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#https://www.vidbm.com/emb.html?xxx=img.vidbm.com/xxx
#https://www.vidbm.com/embed-xxx.html?auto=1

from resources.lib.handler.requestHandler import cRequestHandler
from resources.hosters.hoster import iHoster
from resources.lib.parser import cParser
from resources.lib.packer import cPacker
from resources.lib.comaddon import dialog

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

class cHoster(iHoster):

    def __init__(self):
        self.__sDisplayName = 'vidshare'
        self.__sFileName = self.__sDisplayName
        self.__sHD = ''

    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName + ' [COLOR skyblue]' + self.__sDisplayName + '[/COLOR]'

    def setFileName(self, sFileName):
        self.__sFileName = sFileName

    def getFileName(self):
        return self.__sFileName

    def getPluginIdentifier(self):
        return 'vidshare'

    def setHD(self, sHD):
        self.__sHD = ''

    def getHD(self):
        return self.__sHD

    def isDownloadable(self):
        return False

    def setUrl(self, sUrl):
        self.__sUrl = str(sUrl)
        self.__sUrl = self.__sUrl.replace('embed-', '')

    def getIdFromUrl(self, sUrl):
        sPattern = '\?(.+?)='
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if (aResult[0] == True):
            return aResult[1][0]
        return ''
        
    def checkUrl(self, sUrl):
        return True

    def __getUrl(self, media_id):
        return

    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):

        sUrl = self.__sUrl

        oRequest = cRequestHandler(sUrl)
        sHtmlContent = oRequest.request()

        oParser = cParser()
        sPattern = "<script type='text/javascript'>(.+?)</script>"
        aResult = oParser.parse(sHtmlContent,sPattern)
 

        if (aResult[0] == True):
            sHtmlContent2 = cPacker().unpack(aResult[1][0])


            sPattern2 = '"([^<]+)"],poster'
            aResult = oParser.parse(sHtmlContent2,sPattern2)

            if (aResult[0] == True):
				api_call = aResult[1][0] + '&Referer=' + self.__sUrl

			
 
				
        if (api_call):
            return True, api_call

        return False, False