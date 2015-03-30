
import subprocess as sp
import collections

def stage_server_lines():
    sp.call('git add ../server')
    lines = sp.getoutput('git checkout |grep server')
    return lines

def parse_lines():
    """Return a changes defaultdict
    """
    lines = stage_server_lines().split(sep='\n')
    import pdb; pdb.set_trace()
    changes = collections.defaultdict(list)
    for line in lines:
        if line == '':
            continue
        l = line.split('\t')
        changes[l[0]].append(l[1])
    return changes

def dispatch_action():
    changes = parse_lines()
    adds = changes.get('A')
    if adds:
        do_adds(adds)

def do_adds(adds):
    print(adds)

    
if __name__ == '__main__':
    dispatch_action()
