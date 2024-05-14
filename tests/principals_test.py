from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200
    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B

#added tests for grade assignment
def test_grade_assignment_missing_id(client, h_principal):
    """
    Failure case: Missing assignment ID in the payload
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400
    assert 'error' in response.json

def test_grade_assignment_missing_grade(client, h_principal):
    """
    Failure case: Missing grade in the payload
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4
        },
        headers=h_principal
    )

    assert response.status_code == 400
    assert 'error' in response.json

def test_grade_assignment_invalid_grade(client, h_principal):
    """
    Failure case: Invalid grade in the payload
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': 'Z'  # Assuming 'Z' is not a valid grade
        },
        headers=h_principal
    )

    assert response.status_code == 400
    assert 'error' in response.json

#additional tests for get assigments

def test_get_assignments_unauthorized(client, h_principal):
    # Make a GET request to retrieve assignments without authentication
    response = client.get(
        '/principal/assignments'
    )

    # Assert that the response status code is 401 (Unauthorized)
    assert response.status_code == 401

def test_get_assignments_invalid_token(client, h_principal):
    # Assuming an invalid authentication token
    headers = {'Authorization': 'Bearer invalid_token'}

    # Make a GET request to retrieve assignments with invalid token
    response = client.get(
        '/principal/assignments',
        
    )

    # Assert that the response status code is 401 (Unauthorized)
    assert response.status_code == 401
