from database.db import Student, Jury

async def save_values(student_id, student_name, topic, potok, date, juries_id):
    juries = []
    
    for jury_id in juries_id:
        jury = Jury.objects(jury_id=jury_id).first()
        if jury:
            juries.append(jury)

    student = Student.objects(student_id=student_id).first()
    
    if student:
        student.full_name = student_name
        student.topic = topic
        student.potok = potok
        student.date = date
    else:
        student = Student(student_id=student_id, full_name=student_name, topic=topic, potok=potok, date=date)

    for jury in juries:
        if jury not in student.juries:
            student.juries.append(jury)

    student.save()

    for jury in juries:
        if jury not in student.juries:
            student.juries.append(jury)
            jury.students.append(student)
            jury.save()
