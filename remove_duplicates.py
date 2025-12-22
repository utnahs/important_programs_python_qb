# WAP to remove duplicates from a list (not using membership operator)
def remove_duplicates(old_list):
    new_list=[]
    for i in range(len(old_list)):
        is_duplicate=False
        for j in range(len(new_list)):
            if old_list[i]==new_list[j]:
                is_duplicate=True
        if is_duplicate==False:
            new_list.append(old_list[i])
    return new_list

remove_duplicates([1,1,2,3,2])    
