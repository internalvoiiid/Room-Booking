import pytest

from src.booking_cost import calculate_booking_cost


@pytest.mark.parametrize(
    ("nights", "nightly_rate_cents", "expected"),
    [
        (1, 10000, 10000),
        (3, 10000, 30000),
        (5, 0, 0),
        (30, 10000, 300000),
        (7, 10000, 70000),  # requirement: no free night
        (6, 10000, 60000),  # added: just below the 7-night threshold
        (8, 10000, 80000),  # added: just above the threshold
    ],
)
def test_valid_booking_returns_expected_cost(
    nights,
    nightly_rate_cents,
    expected,
):
    # Arrange

    # Act
    result = calculate_booking_cost(
        nights,
        nightly_rate_cents,
    )

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    ("nights", "nightly_rate_cents"),
    [
        (0, 10000),
        (31, 10000),
        (5, -1),
    ],
)
def test_invalid_range_raises_value_error(
    nights,
    nightly_rate_cents,
):
    with pytest.raises(ValueError):
        calculate_booking_cost(
            nights,
            nightly_rate_cents,
        )


@pytest.mark.parametrize(
    ("nights", "nightly_rate_cents"),
    [
        ("5", 10000),
        (5, "10000"),
        (5.0, 10000),
        (5, 10000.0),
        (True, 10000),
        (5, False),
        (None, 10000),  
        (5, None),      
    ],
)
def test_invalid_type_raises_type_error(
    nights,
    nightly_rate_cents,
):
    with pytest.raises(TypeError):
        calculate_booking_cost(
            nights,
            nightly_rate_cents,
        )