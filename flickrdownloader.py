'''Adaptation from https://gist.github.com/yunjey/14e3a069ad2aa3adf72dee93a53117d6
   Special thanks to: https://gist.github.com/yunjey
'''

import flickrapi
import urllib.request
from PIL import Image
from tqdm import tqdm
import argparse

def downloader(key:str, secret:str, keyword:str, n_pics:int):
    flickr = flickrapi.FlickrAPI(key, secret, cache=True)
    photos = flickr.walk(text=keyword,
                         tag_mode='all',
                         tags=keyword,
                         extras='url_c',
                         per_page=100,           # may be you can try different numbers..
                         sort='relevance')
    for i, photo in enumerate(photos):
        url = photo.get('url_c')
        try:
            urllib.request.urlretrieve(url, f'{keyword}00{i}.jpg')
        except:
            print('URL Invalid {} Skipping'.format(url))
            continue
        print(n_pics)
        if i > n_pics:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage='flickrdownload.py key secret keyword n_pics')
    parser.add_argument('key')
    parser.add_argument('secret')
    parser.add_argument('keyword')
    parser.add_argument('n_pics', type=int)
    args = parser.parse_args()
    downloader(key=args.key, secret=args.secret,
                keyword=args.keyword, n_pics=args.n_pics)
