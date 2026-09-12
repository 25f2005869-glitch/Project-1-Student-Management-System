from flask import Blueprint, render_template, request, redirect, flash
from extensions import db
from models.student import Student

student = Blueprint("student", __name__)


# ==========================
# Add Student
# ==========================
@student.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_data = Student(
            name=request.form["name"],
            roll_no=request.form["roll_no"],
            department=request.form["department"],
            year=request.form["year"],
            phone=request.form["phone"],
            email=request.form["email"],
            address=request.form["address"]
        )

        db.session.add(student_data)
        db.session.commit()

        flash("Student Added Successfully!", "success")

        return redirect("/students")

    return render_template("add_student.html")


# ==========================
# View Students + Search
# ==========================
@student.route("/students")
def students():

    search = request.args.get("search", "").strip()

    if search:

        all_students = Student.query.filter(
            Student.name.ilike(f"%{search}%")
        ).all()

    else:

        all_students = Student.query.all()

    return render_template(
        "students.html",
        students=all_students,
        search=search
    )


# ==========================
# Edit Student
# ==========================
@student.route("/edit-student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student_data = Student.query.get_or_404(id)

    if request.method == "POST":

        student_data.name = request.form["name"]
        student_data.roll_no = request.form["roll_no"]
        student_data.department = request.form["department"]
        student_data.year = request.form["year"]
        student_data.phone = request.form["phone"]
        student_data.email = request.form["email"]
        student_data.address = request.form["address"]

        db.session.commit()

        flash("Student Updated Successfully!", "success")

        return redirect("/students")

    return render_template(
        "edit_student.html",
        student=student_data
    )


# ==========================
# Delete Student
# ==========================
@student.route("/delete-student/<int:id>")
def delete_student(id):

    student_data = Student.query.get_or_404(id)

    db.session.delete(student_data)
    db.session.commit()

    flash("Student Deleted Successfully!", "success")

    return redirect("/students")