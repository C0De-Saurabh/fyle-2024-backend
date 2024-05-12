from flask import Blueprint, request
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher
from .schema import AssignmentSchema, TeacherSchema, AssignmentGradeSchema
from flask import jsonify


principal_resources = Blueprint('principal_resources', __name__)

@principal_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_principal_assignments(p):
    """List all submitted and graded assignments"""
    assignments = Assignment.get_graded_and_submitted_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)


@principal_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teachers = Teacher.query.all()
    teacher_schema = TeacherSchema(many=True)
    teachers_dump = teacher_schema.dump(teachers)
    return jsonify(teachers_dump)

@principal_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_principal_assignment(principal, incoming_payload):
    """Grade or re-grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=principal
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
