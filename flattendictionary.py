def flattern_dict(dic,nestedkey=None,result=None):
    if result is None:
        result=[]
    for key,value in dic.items():
        if isinstance(key,dict):
            flattern_dict(value,key,result)
        else:
            if nestedkey is None:
                result[key]=value
            else:
                result[nestedkey + "." + str(key)]=value
    return result
 #     if isinstance(dic[key],dict):
    #         flattern_dict(key,result,neskey)
    #     else:
    #        x= nestedkey+str(key)
    #        y=x.join(dic[key])
    #        result.append(y)
    # return result
flattern_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})