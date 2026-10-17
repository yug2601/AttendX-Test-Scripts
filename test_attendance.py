def mark_attendance(student_id, status):
    """Simulate attendance marking for AttendX."""
    if not student_id:
        return False
    if status not in ("Present", "Absent"):
        return False
    return True


def test_mark_present():
    assert mark_attendance("STU101", "Present") is True


def test_mark_absent():
    assert mark_attendance("STU102", "Absent") is True


def test_attendance_without_student_id():
    assert mark_attendance("", "Present") is False


def test_invalid_attendance_status():
    assert mark_attendance("STU103", "Late") is False