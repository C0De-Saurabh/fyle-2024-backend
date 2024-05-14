-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH GradedAssignments AS (
    SELECT teacher_id, COUNT(*) AS num_grade_a
    FROM assignments
    WHERE grade = 'A'
    GROUP BY teacher_id
),
MaxGradedTeacher AS (
    SELECT TOP 1 WITH TIES teacher_id
    FROM assignments
    GROUP BY teacher_id
    ORDER BY COUNT(*) DESC
)
SELECT num_grade_a
FROM GradedAssignments
WHERE teacher_id IN (SELECT teacher_id FROM MaxGradedTeacher)

