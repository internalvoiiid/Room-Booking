import pytest

from src.booking_refund import is_refundable


@pytest.mark.parametrize(
    ("hours_before_checkin", "flexible_rate", "expected"),
    [
        (72, True, True),
        (48, True, True),    # requirement: at least 48 hours
        (47, True, False),
        (24, True, False),
        (72, False, False),
        (0, True, False),
        (48, False, False),
    ],
)
def test_refund_eligibility_returns_expected_result(
    hours_before_checkin,
    flexible_rate,
    expected,
):
    # Arrange

    # Act
    result = is_refundable(
        hours_before_checkin,
        flexible_rate,
    )

    # Assert
    assert result is expected


def test_negative_hours_raises_value_error():
    with pytest.raises(ValueError):
        is_refundable(-1, True)


@pytest.mark.parametrize(
    ("hours_before_checkin", "flexible_rate"),
    [
        ("48", True),
        (48, "True"),
        (48, 1),
        (True, True),
        (None, True),

    ],
)
def test_invalid_type_raises_type_error(
    hours_before_checkin,
    flexible_rate,
):
    with pytest.raises(TypeError):
        is_refundable(
            hours_before_checkin,
            flexible_rate,
        )