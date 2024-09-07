def refine_list(input_str: str):
    if input_str == "":
        return ""
    list_odd,list_even = [],[] 
    answer = ""
    for n in input_str:         # 檢查輸入字串中每個數字 n
        if int(n) % 2 == 1:     # 若n為奇數則存入 list_odd
            list_odd.append(int(n))
        else:                   # 若n為偶數則存入 list_even
            list_even.append(int(n))
    for item in sorted(list_odd,reverse=True) + sorted(list_even):  #將 list_odd 與 list_even 分別反續與正續排序再加入 answer 字串中
        answer += str(item)
    return answer


nums = str(input("nums: "))
print(refine_list(nums))