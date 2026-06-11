from flask import Flask, jsonify, request

app = Flask(__name__)

# Student Data
students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "college": "ABC College",
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "Sarah",
        "age": 21,
        "college": "XYZ College",
        "branch": "Electronics"
    },
    {
        "id": 3,
        "name": "David",
        "age": 22,
        "college": "PQR College",
        "branch": "Mechanical"
    }
]

# Home Route
@app.route('/')
def home():
    return "Student Management API is Running!"

# GET All Students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET Student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

# Search Student by Name
@app.route('/search-student/<name>', methods=['GET'])
def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

# Add Student
@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "age": data["age"],
        "college": data["college"],
        "branch": data["branch"]
    }

    students.append(new_student)

    return jsonify({"message": "Student Added Successfully"}), 201

# Delete Student
@app.route('/delete-student/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student Deleted Successfully"})

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)