import json
from pprint import pprint

def magic_sort(fmt_dict):
    # Hold JSON representation of these objects
    rdcd_dict = {}
    dep_list = {}
    for obj,body in fmt_dict.iteritems():
        tmp_obj = {'string':json.dumps({obj:body})}
        for attr,egl_type in body.iteritems():
            if egl_type not in ('int','string','real'):
                tmp_obj[attr] = egl_type
                if attr not in dep_list:
                    dep_list[attr] = []
                dep_list[attr].append(obj)
        rdcd_dict[obj] = tmp_obj

    # Hold dependency ordering of eagle objects
    tmp_list = []
    multi = {}
    for obj,deps in dep_list.iteritems():
        if len(deps) == 1:
            if deps[0] in tmp_list:
                tmp_list.insert(tmp_list.index(deps[0])+1, obj)
            else:
                tmp_list.insert(0,obj)
        else:
            multi[obj] = deps

    for obj,deps in multi.iteritems():
        final_index = 0
        for i in deps:
            if i in tmp_list and i > final_index:
                final_index = tmp_list.index(i)

        if final_index > 0:
            final_index += 1
        tmp_list.insert(final_index, obj)

    return tmp_list, dep_list

if __name__ == '__main__':
    eagle_fmt = ''
    with open('eagle.json', 'r') as fmt_file:
        eagle_fmt = json.loads(''.join(fmt_file.readlines()))

    pprint(magic_sort(eagle_fmt))
