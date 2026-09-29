# doing all the math calculations here

def total_minutes(data):
    sum = 0
    for item in data:
        # index 2 has the minutes
        sum = sum + int(item[2]) 
    return sum

def calc_productivity(data):
    tot = total_minutes(data)
    if tot == 0:
        return 0.0
    
    good_time = 0
    for item in data:
        # index 1 has the category
        if item[1] == "Productive" or item[1] == "Education":
            good_time = good_time + int(item[2])
            
    ans = (good_time / tot) * 100
    return round(ans, 2)
    
def get_category_sums(data):
    # empty dictionary to store totals for each type
    cat_dict = {}
    for item in data:
        cat = item[1]
        mins = int(item[2])
        
        if cat in cat_dict:
            cat_dict[cat] = cat_dict[cat] + mins
        else:
            cat_dict[cat] = mins
            
    return cat_dict