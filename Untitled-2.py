with open('./log_files/201811113010.log',encoding='utf8')as file:
    x = 0
    for line in file:
        student_id = line.split(',')[1]
        student_id = student_id.split(':')[1]
        if student_id==201811113010:
            x=x+1

    print(x)

