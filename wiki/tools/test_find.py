'''
需求: 输入 [
        {id:1,parent_id:0},
        {id:2,parent_id:1},
        {id:3,parent_id:0},
        {id:4,parent_id:3},
      ]

输出结果:
        [
        {id:1,children:[{id:2}...]},
        {id:3,children:[{id:4}...]}
        ]
'''
def find_father(input_list):
    home = {}
    parent_list = []
    for data in input_list:
        if data['parent_id'] == 0:
            #爹
            parent_list.append({'id':data['id']})
        else:
            p_id = data['parent_id']
            if p_id not in home:
                home[p_id] = []
                home[p_id].append({'id':data['id']})
            else:
                home[p_id].append({'id':data['id']})

            #等价以上if else代码
            # home.setdefault(p_id,[])
            # home[p_id].append({'id':data['id']})

    for f in parent_list:
        if f['id'] in home:
            f['children'] = home[f['id']]
    return parent_list















