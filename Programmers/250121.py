def solution(data, ext, val_ext, sort_by):
    answer = []
    data_list = []
    for d in data:
        item = {
            "code": d[0],
            "date": d[1],
            "maximum": d[2],
            "remain": d[3]
        }
        data_list.append(item)
        
    query1 = [item for item in data_list if item[ext] < val_ext]
    query1.sort(key=lambda x: x[sort_by])
    for q in query1:
        answer.append([q["code"],q["date"],q["maximum"],q["remain"]])