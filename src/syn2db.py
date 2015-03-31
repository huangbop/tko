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
    import pdb; pdb.set_trace()
    if not changed_json_files == {}:
        do_commit(changed_json_files)

def do_adds(adds):
    for add_file in adds:
        import pdb; pdb.set_trace()
        file_name = add_file[add_file.rindex('/') + 1 : -5]
        info = json.load(open('../%s' % add_file))
        info['name'] = file_name
        rest.add_record('product', info)

def do_commit(files):
    sp.call('git commit -m "******** %s"' % str(files))


if __name__ == '__main__':
    dispatch_action()
