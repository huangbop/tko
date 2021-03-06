"""*
"""
import subprocess as sp
import collections

import rest
import json


def product_checkout_useful_string():
    import pdb; pdb.set_trace()
    sp.call('git add ../server/')
    useful_string = sp.getoutput("git checkout |grep 'server/' |iconv -f UTF-8")
    return useful_string


def parse_useful_string():
    """Return a changed defaultdict
    """
    useful_lines = product_checkout_useful_string().split(sep='\n')
    changed_files = collections.defaultdict(list)
    for line in useful_lines:
        if line == '':
            continue
        pairs = line.split('\t')
        changed_files[pairs[0]].append(pairs[1])
    return changed_files


def dispatch_action():
    changed_files = parse_useful_string()
    adds = changed_files.get('A')
    if adds:
        do_adds(adds)
    modify = changed_files.get('M')
    if modify:
        do_modify(modify)
    delete = changed_files.get('D')
    if delete:
        do_delete(delete)
    import pdb; pdb.set_trace()
    if not changed_files == {}:
        do_commit(changed_files)


def delete_image(delete_file):
    """*
    """
    file_name = delete_file[delete_file.rindex('/') + 1:]
    info = {'name': file_name}
    rest.delete_image(info)


def delete_json(delete_file):
    """*
    """
    import pdb; pdb.set_trace()
    file_name = delete_file[delete_file.rindex('/') + 1: -5]
    info = {'name': file_name}
    rest.delete_product(info)


def do_delete(delete):
    """*
    """
    for delete_file in delete:
        import pdb; pdb.set_trace()
        if delete_file.find('images') != -1:
            delete_image(delete_file)
        elif delete_file.find('products') != -1:
            delete_json(delete_file)

def modify_image(modify_file):
    """*
    """
    file_name = modify_file[modify_file.rindex('/') + 1:]
    file_type = modify_file[modify_file.rindex('.') + 1:]
    file_bin = open('../server/images/' + file_name, 'rb')
    info = {'name': file_name, 'type': file_type, 'bin': file_bin}
    rest.modify_image(info)


def modify_json(modify_file):
    """*
    """
    import pdb; pdb.set_trace()
    file_name = modify_file[modify_file.rindex('/') + 1: -5]
    info = json.load(open('../%s' % modify_file))
    info['name'] = file_name
    rest.modify_product(info)


def do_modify(modify):
    """*
    """
    for modify_file in modify:
        import pdb; pdb.set_trace()
        if modify_file.find('images') != -1:
            modify_image(modify_file)
        elif modify_file.find('products') != -1:
            modify_json(modify_file)


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
    import pdb; pdb.set_trace()
    file_name = add_file[add_file.rindex('/') + 1: -5]
    info = json.load(open('../%s' % add_file))
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
    import pdb; pdb.set_trace()
    sp.call('git commit -a -m "**** %s"' % str(files))
    pass


if __name__ == '__main__':
    dispatch_action()
