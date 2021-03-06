#-*- coding: utf-8 -*-

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

def song_data_list(rank):

    import urllib2
    from BeautifulSoup import BeautifulSoup
    from urlparse import urljoin
    import datetime

    d = datetime.datetime.today() #現在の時刻を取得

    result = [] #結果を格納する配列

#Vocaloidカテゴリのランキングのhtmlを取得
    url = "http://www.nicovideo.jp/ranking/fav/daily/vocaloid"
    html = urllib2.urlopen(url).read()

#BeautifulSoupでパース
    soup = BeautifulSoup(html)

#30位までの曲データを取得
    for i in range(rank):
        songId = "item" + str(i+1)
        song = soup.find("div", {"id":songId}) #(i+1)位の曲のデータが入っている部分を取り出す
        songdata = song.find("a",{"class":"watch"}) #タイトル、リンクが記述されている部分を取得
        songtitle = dict(songdata.attrs)["title"] #タイトルを取得
        songurl = urljoin("http://www.nicovideo.jp", dict(songdata.attrs)["href"]) #リンクを取得
        songdate = song.findAll("span")[4].find("strong").contents[0] #投稿日時を取得

        result.append(songdate)
        result.append(str(i+1) + "位 ".decode("utf-8") + songtitle + "(" + songurl + ") at " + str(gh(d.hour)) + ":" + gm(d.minute))

    
    return result

if __name__ == "__main__":
    for node in  song_data_list(30):
        print node.encode("utf-8")
