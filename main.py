#!/usr/bin/env python
# -*- coding: utf-8 -*-

#テストコミット
#プルリクのテスト

import sys
import twitter
from GetSongData import song_data_list

#てすとぼっと
CONSUMER_KEY='2CZc0GISVaQKWkif36OyXQ'
CONSUMER_SECRET='reFXlASxN0S2zvQ5DEFp485FT0MoocgWHAUWQ70M1Y'
ACCESS_TOKEN='591900747-MeLBEOABx5fqrmiVlfqZMlYcNCXVEKCLKasDnsYj'
ACCESS_TOKEN_SECRET='JgWKdmClR0XZ67DxmY62NV8tnou82gfskDK2tZ8WNM'

#てすとぼっと２ @d81609
CONSUMER_KEY2="plwBOVRqAMQd7wS4KTPTg"
CONSUMER_SECRET2="FPcy2FVta94krxRi3vA1LnHVNREypkQAoDowESTIU"
ACCESS_TOKEN2="597458284-TmyuUEIaDzt8Zm3rJt8HjpxrWL2PnjBUklxAoUFN"
ACCESS_TOKEN_SECRET2="5XcG3onvjCzokRhPKXIyVSNq8A3b3duoVvHNNky9g4c"

api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)


print "Content-Type: text/plain"
print ""

#hourを文字列として返す
def gh(h):
    if h < 15: #日本との時差を考えて
        return h+9
    else:
        return h-15

#minuteを文字列として返す
def gm(m):
    if m < 10:
        return "0" + str(m) #1桁なら0を左に追加
    else:
        return str(m)

def rank_today():
    import urllib2
    import re
    import datetime
    import sys
    Rank = 30 #上位30位までを取得
    result = []
    d = datetime.datetime.today()
    p = 'a\sclass.+a>'
    p2 = "\d+年\d+月\d+日\s\d+:\d+"
    rank = 1
    time = 0
    s = song_data_list(30)
    """
    for line in urllib2.urlopen("http://www.nicovideo.jp/ranking/fav/dayly/vocaloid"):
        regex = re.compile(p)
        regex2 = re.compile(p2)
        match = regex.search(line)
        match2 = regex2.search(line)
        if match is not None:
            title = match.group().decode("utf-8")
            link = title.split("f")[1].split(">")[0][2:-1]
            title = title.split(">")[1].split("<")[0]
            s.append(str(rank) + "位 ".decode("utf-8") + title + "(http://www.nicovideo.jp/" + link + ") at " + str(gh(d.hour)) + ":" + gm(d.minute))
            rank = rank + 1
        if match2 is not None:
            time = time + 1
            if time > 0:
                s.append(match2.group().decode("utf-8"))
    """
    f = 0
    rank = 0
    for i in s:
        if rank > Rank - 1:
            break
        try:
            temp =  i.index("年".decode("utf-8"))
            year = int(i.split("年".decode("utf-8"))[0])
            month = int(i.split("年".decode("utf-8"))[1].split("月".decode("utf-8"))[0])
            day = int(i.split("月".decode("utf-8"))[1].split("日".decode("utf-8"))[0])
            if datetime.date(d.year,d.month,d.day) - datetime.date(year,month,day) < datetime.timedelta(2) or rank < 3:
                print i.encode("sjis")
                f = 1
        except ValueError:
            rank = rank + 1
            if f == 1:
                try:
                    print i.encode("sjis")
                    print len(i.encode("utf-8"))
                    result.append(i.encode("utf-8"))
                    f = 0
                except:
                    f = 0
                    title = ""
                    for w in range(0,len(i)):
                        try:
                            sys.stdout.write(i[w].encode("sjis"))
                            title += i[w]
                        except:
                            sys.stdout.write("?")
                            title += "?"
                    sys.stdout.write("\n")
                    print len(i.encode("utf-8"))
                    print "mojibake"
                    result.append(i.encode("utf-8"))
    return result

#文字列のバイト数を取得
def cut(num):
    num = num/3
    return num*3

hoken = []
body = ""

for i in reversed(rank_today()):
    if len(i) > 140:
        i = i.split("(")[0][0:cut(130-len(i))] + "... (".encode("utf-8") + i.split("(")[1]
    try:
        #pass
        body += i
        api.PostUpdate(i)
        print "post success"
    except:
        print "post failed"
        hoken.append(i)

for i in hoken:
    try:
        api.PostUpdate(i)
    except:
        print "post failed 2"


