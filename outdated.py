month_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

date = input("date: ")
if "/" in date:
    x, y, z = date.split("/")
    x_1 = int(x)
    if x_1 < 10:
        x_1 = f"0{x_1}"
    y_1 = int(y)
    if y_1 < 10:
        y_1 = f"0{y_1}"
    z_1 = int(z)
    if x_1 > 31:
        pass
    if y_1 > 12:
        pass
    else:
        print(z_1, "-", x_1, "-", y_1, sep="")
else:
    if "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in month_list:
            month = month_list.index(month) + 1
            day = int(day)
            if day > 31:
                pass
            elif day < 10:
                day = f"0{day}"
            print(year, "-", month, "-", day, sep="")
    

    
    
        
        

