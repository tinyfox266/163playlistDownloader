#! /usr/bin/python
import sys, urllib, os, json

def report_hook(count, block_size, total_size):
    print '%02d%%'%(100.0 * count * block_size/ total_size)

playlist_id = sys.argv[1]

info_url="http://music.163.com/api/playlist/detail?id="+playlist_id

req = urllib.urlopen(info_url).read();

songs_info = json.loads(req);

playlist_name = songs_info['result']['name']

if (os.path.exists(playlist_name) == False):
    os.mkdir(playlist_name)

for item in songs_info["result"]["tracks"]:
    song = item['name']
    url = item['mp3Url']
    print "start to download " + song
    mp3file = urllib.urlretrieve(url,playlist_name+ '/' + song+'.mp3', reporthook=report_hook)
    print song+ " has been downloaded"

