import math_calcs

def print_report(data):
    tot = math_calcs.total_minutes(data)
    prod = math_calcs.calc_productivity(data)
    
    print("\n***********************************")
    print("        MY DIGITAL HABITAT         ")
    print("***********************************")
    print("Total Mins Used :", tot)
    print("Productivity %  :", prod)
    
    print("--- Health Status ---")
    if tot > 300:
        print("Warning: You are using the screen too much!")
    elif prod < 30:
        print("Bad: You are wasting time on useless apps.")
    else:
        print("Good: You have a healthy digital life.")
    print("***********************************\n")

def print_bar_chart(data):
    cats = math_calcs.get_category_sums(data)
    if len(cats) == 0:
        print("No data available.")
        return
        
    print("\n--- APP CATEGORY USAGE ---")
    for c in cats:
        # dividing by 10 to make stars for the graph
        num_stars = int(cats[c] / 10)
        stars = "*" * num_stars
        print(c, ":", cats[c], "mins |", stars)
    print("\n")