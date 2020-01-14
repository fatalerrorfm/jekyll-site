import feedparser
import os
import re

post_names = {}

root_dir = "/Users/soroushkhanlou/Desktop/fatalerror"

for f in os.listdir(root_dir + "/_posts"):
    if f == 'rename.rb' or f == '2018-05-23-episode-70-will-be-a-live-show-at-wwdc.html':
        # ep70 is confusing; handle it manually
        continue
    parts = f.split("-")
    title_part = '-'.join(parts[3:])
    ep_num = re.findall(r'^[^\d]*(\d+)', title_part)[0]
    post_names[ep_num] = f

d = feedparser.parse("./episodes.rss")

def copy_value(rss_dict, lines, key):
    if key in rss_dict:
        lines.append('{}: {}\n'.format(key, e[key]))

for e in d.entries:
    if e.guid == '578d8d3bf5e231fc9f850e55:578d8eaebe65944d662e0687:5b0595392b6a287c58f9f70d':
        # ep70 is confusing; handle it manually
        continue
    ep_num = re.findall(r'^[^\d]*(\d+)', e.title)[0]
    fname = post_names[ep_num]
    with open(root_dir + "/_posts/"+fname, "r") as infile:
        lines = infile.readlines()
        new_lines = lines[:2]
        copy_value(e, new_lines, "guid")
        copy_value(e, new_lines, "itunes_season")
        new_lines = new_lines + lines[2:]
    with open(root_dir + "/_posts/"+fname, "w") as outfile:
        outfile.write(''.join(new_lines))

