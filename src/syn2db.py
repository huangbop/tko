import subprocess as sp
import collections

import rest
import json


def product_checkout_useful_string():
    sp.call('git add ../server/product')
    useful_string = sp.getoutput("git checkout |grep 'product/.*.json'").encode('gbk').decode()
    return useful_string

def parse_useful_string():
    """Return a changed defaultdict
    """
    useful_lines = product_checkout_useful_string().split(sep='\n')
    changed_json_files = collections.defaultdict(list)
    for line in useful_lines:
        if line == '':
            continue
        pairs = line.split('\t')
        changed_json_files[pairs[0]].append(pairs[1])
    return changed_json_files

def dispatch_action():
    changed_json_files = parse_useful_string()
    adds = changed_json_files.get('A')
    if adds:
        do_adds(adds)

def do_adds(adds):
    for add_file in adds:
        import pdb; pdb.set_trace()
        info = open('../%s' % add_file, 'rb').read()
        rest.add_record('product', info)


if __name__ == '__main__':
    dispatch_action()
