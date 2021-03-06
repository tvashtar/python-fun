'''
This is a collection of utility functions for use in python_fun notebooks and scripts
Author: Conor Laver
License: MIT
'''

def summarize_dict(my_dict, max_expand=10, max_depth=3, key='Initial Object', depth=0):
    ''' This function will recursively pretty print a nested dict. 
    max_expand sets how long a dict can be that will be fully expanded
    max_depth sets how deep in the recursion the nested data will expand to
    '''
    
    depth += 1
    print('    '*depth + f'{key}: {type(my_dict)} with {len(my_dict)} elements')
    if depth > max_depth:
        return
    if len(my_dict.keys()) <=  max_expand:
        for item in my_dict.keys():
            if isinstance(my_dict[item], (int, float, complex, str, tuple)):
                print('    '*(depth+1) + f'{item}: {my_dict[item]}')
            elif isinstance(my_dict[item], list):
                summarize_list(my_dict[item], max_expand, max_depth, key=item, depth=depth)
            elif isinstance(my_dict[item], dict):
                summarize_dict(my_dict[item], max_expand, max_depth, key=item, depth=depth)
                
def summarize_list(my_list, max_expand, max_depth, key='Top Level', depth=0):
    ''' Thus fuction will recursively pretty print a nested list
    max_expand sets how long a list can be that will be fully expanded
    max_depth sets how deep in the recursion the nested data will expand to
    '''
    
    depth += 1
    print('    '*depth + f'{key}: {type(my_list)} with {len(my_list)} elements')
    if depth > max_depth:
        return
    if len(my_list) <=  max_expand:
        for item in my_list:
            if isinstance(item, (int, float, complex, str, tuple)):
                print('    '*(depth+1) + f'{item}')
            elif isinstance(item, list):
                summarize_list(item, max_expand, max_depth, key='', depth=depth)
            elif isinstance(item, dict):
                summarize_dict(item, max_expand, max_depth, key='', depth=depth)
