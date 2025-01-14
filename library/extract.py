# Name     : Youtube_Downloader 'Inline' [ Telegram ]
# Repo     : https://github.com/hasithamadhusanka/Youtube_Downloader
# Author   : Hasitha Madhushanka

from youtubesearchpython import *

async def youtube_search(query):
    search = VideosSearch(query)
    result = search.result()['result']
    return result

async def yt_link_search(url):
    videoInfo = Video.getInfo(url, mode=ResultMode.dict)
    return videoInfo

