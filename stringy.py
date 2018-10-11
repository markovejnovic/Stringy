#!/usr/bin/env python

import argparse
import os.path
import json
import re

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('strings', help='The file containing the string \
            insertion definitions', type=lambda x: is_valid_file(parser, x))
    parser.add_argument('to_process', help='The file to insert into',
            type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()

    with open(args.strings, 'r') as f:
        strings = json.load(f)

    content = None
    with open(args.to_process, 'r') as f:
        content = f.read()
    
    for key in strings:
        content = re.sub(r'{# ' + key + r' #}', 
                strings[key],
                content, flags=re.M)

    with open(args.to_process, 'w') as f:
        f.write(content)

