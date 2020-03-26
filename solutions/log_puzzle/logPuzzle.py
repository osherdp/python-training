#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib.request import urlretrieve as url_ret

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(urls_file_name):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order.
    The wanted urls are in this format "/python/logpuzzle/photo_name.jpg".
    """

    prefix_url = r"http://data.cyber.org.il"
    lst_result_url = []
    # Finding a "GET" and ".jpg" substrings, and check if they made from the same url.
    index_start_url = 0
    with open(urls_file_name, 'r') as f:
        content = f.read()

        # If there is no more urls -(index = -1) because we adding the index 4 in the next line
        while index_start_url != -1 + 4:

            # The num of characters between G and / in "GET /python..."
            index_start_url = content.find("GET") + 4

            # The num of characters between "." and the end of ".jpg",
            # We want that the stop index will be bigger the the start index
            index_stop_url = content[index_start_url:].find(".jpg") + index_start_url + 4

            # Checks if the url is in the wanted format - "/python/logpuzzle/photo_name.jpg"
            if content[index_start_url: index_start_url + len("/python/logpuzzle/")] == "/python/logpuzzle/":
                lst_result_url.append(prefix_url + content[index_start_url: index_stop_url])

            content = content[index_start_url:]

    # Sorting the url list according to the photo name, filtering the repeating urls
    lst_result_url = organized_url_lst(lst_result_url, urls_file_name)

    return lst_result_url


def organized_url_lst(lst_url, urls_file_name):
    """
    Sorting the url list according to the photo name, filtering the repeating urls.
    The sorting way woult be accordong to the urls_file_name -  "logo_data.cyber.org.il" or "message_data.cyber.org.il".
    :param lst_url: The url list that needs to be sorted.
    :param urls_file_name: "logo_data.cyber.org.il" or "message_data.cyber.org.il".
    if "logo_data.cyber.org.il" the sorting way is according the photo name, regular sorting.
    if "message_data.cyber.org.il" the sorting way is according the second part of the photo name.
    example - photo_name = "a-bbbb-cccc.jpg",  the urls would be sorted according to the -"cccc" part.
    :return:
    """
    # Making dictionary - {photo_name: url}
    dict_name_vs_url = {}

    for url in lst_url:
        photo_name = finding_photo_name(url)
        if photo_name not in dict_name_vs_url:
            dict_name_vs_url[photo_name] = url

    # The photo name would be sorted according to the urls_file_name.
    lst_name_sorted = []
    if urls_file_name == r"logo_data.cyber.org.il":
        lst_name_sorted = sorted(dict_name_vs_url.keys())
    if urls_file_name == "message_data.cyber.org.il":
        lst_name_sorted = sorted(dict_name_vs_url.keys(), key=lambda s: s[7:])

    sorted_url_lst = []
    for name in lst_name_sorted:
        sorted_url_lst.append(dict_name_vs_url[name])
    return sorted_url_lst


def finding_photo_name(url):
    """
    Finding the photo name substring in the url string.
    :param url: url string. in this format:  r"http://data.cyber.org.il/python/logpuzzle/photo_name.jpg"
    :return: The photo name
    """
    index_start_file_name = -1
    while url[index_start_file_name] != r'/':
        index_start_file_name -= 1
    file_name = url[index_start_file_name + 1:]
    return file_name


def download_images(img_urls_lst, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.

    :param img_urls_lst: The sorted and organized list of photo urls.
    :param dest_dir: destination directory of the wanted html file.
    """
    lst_image_names = []
    for img_url in img_urls_lst:
        # Saving the photo in a folder "logPuzzle_photos" in name img(num) - the num according to index.
        image_name = "img%d.jpg" % img_urls_lst.index(img_url)
        image_name = os.path.join("logPuzzle_photos", image_name)

        # Downloading the photos according to their url as image_name.
        url_ret(img_url, image_name)

        # Making a list with the image file names including path from root.
        lst_image_names.append(image_name)

    # Making html file with all the photos that are downloaded.
    html_maker(lst_image_names, dest_dir)


def html_maker(lst_image_names, dest_dir):
    """
    Making html file with all the photos that are downloaded.
    Using format html writing:
    content = "<verbatim>\n<html>\n<body>\n<img src='img0_root_path'><img src='img1_root_path'\n</body>
    \n</html>\n" % (file_name, file_name2)
    :param lst_image_names: list of image name that are downloaded, including the path from root.
    :param dest_dir: The name of the wanted html file. (Path from root)
    """
    #

    str_addition_to_content = ""
    for file_name in lst_image_names:
        str_addition_to_content += "<img src='%s'>" % file_name
    content = "<verbatim>\n<html>\n<body>\n%s\n</body>\n</html>\n" % str_addition_to_content

    with open(dest_dir, 'w') as f:
        f.write(content)


def main():
    """
    The parameters given to pychar in this format:
    "--todir" dest_directory urls_file_name

    dest_directory - destination directory of the wanted html file. (path from root) example "logPuzzle.html"
    urls_file_name - "logo_data.cyber.org.il" or "message_data.cyber.org.il"
    """
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
