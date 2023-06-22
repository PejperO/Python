import smtplib

students = {}


def load_data():
    with open('../data/students.txt', 'r') as file:
        for line in file:
            if line.strip():
                email, name, surname, points, grade, status = line.strip().split(',')
                students[email] = {
                    'name': name,
                    'surname': surname,
                    'points': int(points),
                    'grade': int(grade) if grade else None,
                    'status': status
                }


def save_data():
    with open('../data/students.txt', 'w') as file:
        for email, data in students.items():
            file.write(
                f"{email},{data['name']},{data['surname']},{data['points']},{data['grade'] or ''},{data['status']}\n")


def auto_grade():
    for email, data in students.items():
        if data['status'] != 'GRADED' and data['status'] != 'MAILED':
            points = data['points']
            if points >= 90:
                data['grade'] = 5
            elif points >= 75:
                data['grade'] = 4
            elif points >= 60:
                data['grade'] = 3
            elif points >= 45:
                data['grade'] = 2
            else:
                data['grade'] = 1
            data['status'] = 'GRADED'


def remove_student(email):
    if email in students:
        del students[email]
        print('Student removed successfully.')
        save_data()
    else:
        print('Error: Email not found.')


def add_student(email, name, surname, points):
    if email in students:
        print('Error: Email already exists.')
    else:
        students[email] = {
            'name': name,
            'surname': surname,
            'points': points,
            'grade': None,
            'status': ''
        }
        print('Student added successfully.')
        save_data()


def send_email(email, grade):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your_email@gmail.com'
    from_password = 'your_email_password'
    to_email = email
    subject = 'Fundamentals of Python Programming - Grade'
    body = f"Dear student," \
           f"\n\nYour final grade for Fundamentals of Python Programming is: {grade}" \
           f"\n\nBest regards," \
           f"\nYour Instructor"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, f'Subject: {subject}\n\n{body}')
        server.quit()
        print('Grade email sent successfully.')
    except Exception as e:
        print('Error sending email:', str(e))


load_data()
while True:
    print('\n1. Auto Grade\n2. Add Student\n3. Remove Student\n4. Send Grade Email\n5. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        auto_grade()
        save_data()
        print('Automatic grading done.')

    elif choice == '2':
        email = input('Enter student email: ')
        name = input('Enter student name: ')
        surname = input('Enter student surname: ')
        points = int(input('Enter points obtained: '))
        add_student(email, name, surname, points)

    elif choice == '3':
        email = input('Enter student email: ')
        remove_student(email)

    elif choice == '4':
        for email, data in students.items():
            if data['status'] != 'MAILED':
                grade = data['grade']
                if grade is not None:
                    send_email(email, grade)
                    data['status'] = 'MAILED'
                else:
                    print(f"Error: Grade not available for student with email {email}.")
        save_data()

    elif choice == '5':
        print('Exiting...')
        break

    else:
        print('Invalid choice. Please try again.')
