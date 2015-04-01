"""*
"""
import subprocess as sp
import collections

import rest
import json


def product_checkout_useful_string():
    import pdb; pdb.set_trace()
    sp.call('git add ../server/')
    useful_string = sp.getoutput("git checkout").encode('utf16')
    # |grep 'server/.*.[jpg|png|json]'")
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


def add_image(add_file):
    """*
    """
    file_name = add_file[add_file.rindex('/') + 1:]
    file_type = add_file[add_file.rindex('.') + 1:]
    file_bin = open('../server/images/' + file_name, 'rb')
    info = {'name': file_name, 'type': file_type, 'bin': file_bin}
    rest.add_image(info)


def add_json(add_file):
    """*
    """
    file_name = add_file[add_file.rindex('/') + 1: -5]
    info = json.load(open('../products/%s' % add_file))
    info['name'] = file_name
    rest.add_product(info)


def do_adds(adds):
    """*
    """
    for add_file in adds:
        import pdb; pdb.set_trace()
        if add_file.find('images') != -1:
            add_image(add_file)
        elif add_file.find('products') != -1:
            add_json(add_file)


def do_commit(files):
    """*
    """
    # sp.call('git commit -m "******** %s"' % str(files))
    pass


if __name__ == '__main__':
    dispatch_action()
