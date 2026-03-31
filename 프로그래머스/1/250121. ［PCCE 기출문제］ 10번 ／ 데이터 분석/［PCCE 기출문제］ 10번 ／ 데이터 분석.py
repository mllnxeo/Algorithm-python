def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    filtered = []
    for i in data:
        if i[idx[ext]] < val_ext:
            filtered.append(i)
    
    filtered.sort(key=lambda x: x[idx[sort_by]])
    return filtered