﻿#-*- coding: utf-8 -*-
#zombi.(@geekzombi)
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress
from resources.lib.util import cUtil
import re

SITE_IDENTIFIER = 'beinsports_net'
SITE_NAME = 'beinsports.com'
SITE_DESC = 'sport vod'

URL_MAIN = 'http://www.beinsports.com'
SPORT_FOOT = ('https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88', 'showMovies')
SPORT_SPORTS = ('https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88', 'showMovies')
SPORT_GENRES = ('http://', 'showGenres')
SPORT_SPORTS = ('http://', 'load')


URL_SEARCH = ('http://www.beinsports.com/ar/search?q=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://frenchstream.org/les-plus-vues')
    oGui.addDir(SITE_IDENTIFIER, 'showGenres', 'Sports', 'genres.png', oOutputParameterHandler)    
            
    oGui.setEndOfDirectory()
  
def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://www.beinsports.com/ar/search?q='+sSearchText+'&ft=%22%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88%22'  
            showMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
    
    
def showGenres():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ["كرة القدم ","https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["الدوري الإنكليزي الممتاز","https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%86%D9%83%D9%84%D9%8A%D8%B2%D9%8A-%D8%A7%D9%84%D9%85%D9%85%D8%AA%D8%A7%D8%B2/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["دوري أبطال أوروبا","https://www.beinsports.com/ar/%D8%AF%D9%88%D8%B1%D9%8A-%D8%A3%D8%A8%D8%B7%D8%A7%D9%84-%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["الدوري-الإسباني","https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D8%B3%D8%A8%D8%A7%D9%86%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["الدوري الإيطالي","https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%8A%D8%B7%D8%A7%D9%84%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["الدوري الفرنسي","https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D9%81%D8%B1%D9%86%D8%B3%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["تنس","https://www.beinsports.com/ar/%D8%AA%D9%86%D8%B3/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["كرة السلة","https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D8%B3%D9%84%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["رياضات ميكانيكية","https://www.beinsports.com/ar/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A7%D8%AA-%D9%85%D9%8A%D9%83%D8%A7%D9%86%D9%8A%D9%83%D9%8A%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    liste.append( ["BOXE","https://www.beinsports.com/ar/%D8%A7%D9%84%D9%85%D9%84%D8%A7%D9%83%D9%85%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"] )
    
	            
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory() 


def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('&quot;', '"')
    sPattern = ' <img data-sizes="auto" data-src="([^<]+)" data-srcset=".+?class="lazyload".+?</a>.+?<a class="link-picto" href="([^<]+)" onclick=".+?">.+?<span class="picto-1">.+?class="icon-play-1"></i>.+?</span>.+?</a>.+?</div>.+?<span class="time">([^<]+)</span>.+?<div class="category">([^<]+)</div>.+?<figcaption>.+?<a href=".+?">([^<]+)</a>'
   
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            sUrl = str(aEntry[1])
            sInfo = '[COLOR aqua]'+str(aEntry[2])+" //[/COLOR]"+'[COLOR yellow]'+str(aEntry[3])+'[/COLOR]'
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[4]))
            oOutputParameterHandler.addParameter('sThumbnail', str(aEntry[0]))
            oGui.addMisc(SITE_IDENTIFIER, 'showHosters', aEntry[4], 'doc.png', aEntry[0], sInfo, oOutputParameterHandler)

        progress_.VSclose(progress_)
            
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

# ([^<]+) .+?
def __checkForNextPage(sHtmlContent):
    sPattern = '<link rel="next" href="([^<]+)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        aResult = aResult[1][0]
        return aResult

    return False
    

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    #sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/plugins/like.php','').replace('<iframe src="http://www.facebook.com/plugins/likebox.php','')
               
        
    sPattern = '<meta itemprop="embedURL" content="([^<]+)" />'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
            
            url = str(aEntry)
            if url.startswith('//'):
                url = 'http:' + url
            
            sHosterUrl = url
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        progress_.VSclose(progress_) 
                
    oGui.setEndOfDirectory()
    
