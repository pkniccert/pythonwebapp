from faker import Faker
import random
from .models import *
from django.db.models import Sum

fake = Faker()


def create_agency(n=10):
    try:
        for _ in range(n):
            Agency.objects.create(
                code = f'AGNC{random.randint(0, 100)}',
                name = f'Agency{random.randint(0, 100)}'
            )
    except Exception as e:
        print(e)

def create_category(n=10):
    try:
        for _ in range(n):
            Category.objects.create(
                code = f'CATGRY{random.randint(0, 100)}',
                name = f'Category{random.randint(0, 100)}'
            )
    except Exception as e:
        print(e)

def create_subcategory(n=4):
    try:
        categories = Category.objects.all()
        for row in categories:
            Subcategory.objects.create(
                category = row,
                code = f'SUBCATGRY{random.randint(0, 100)}',
                name = f'Subcategory{random.randint(0, 100)}'
            )
    except Exception as e:
        print(e)
        

# def create_subject_marks(n):
#     try:
#         student_objs = Student.objects.all()
#         for student in student_objs:
#             subjects = Subject.objects.all()
#             for subject in subjects:
#                 SubjectMarks.objects.create(
#                     subject = subject,
#                     student = student,
#                     marks = random.randint(0, 100)
#                 )
#     except Exception as e:
#         print(e)


# def seed_db(n=10) -> None:
#     try:
#         for _ in range(n):
#             depart_objs = Department.objects.all()
#             if not depart_objs.exists():
#                 print("No departments found in the database.")
#                 return

#             random_index = random.randint(0, len(depart_objs) - 1)
#             department = depart_objs[random_index]

#             student_id = f"STU-0{random.randint(100, 999)}"
#             name = fake.name()
#             email = fake.email()
#             phone = fake.phone_number()  # Use fake.phone_number() to generate a phone number
#             age = random.randint(20, 30)
#             address = fake.address()

#             student_id_obj = StudentID.objects.create(student_id=student_id)

#             student_obj = Student.objects.create(
#                 department=department,
#                 student_id=student_id_obj,  # Assuming you want to link to the StudentID instance
#                 name=name,
#                 email=email,
#                 phone=phone,
#                 age=age,
#                 address=address,
#             )

#     except Exception as e:
#         print(f"An error occurred: {e}")

# def generate_report_card():
#     try:
#      ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-age')
#      i = 1
#      for rank in ranks:
#         ReportCard.objects.create(
#             student = rank,
#             student_rank = i
#         )
#         i = i + 1
#     except Exception as e:
#         print(f"An error occurred: {e}")