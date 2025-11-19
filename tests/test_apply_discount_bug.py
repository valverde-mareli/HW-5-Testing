from pricing import apply_discount

def test_apply_discount_bug():
	"""

	Regression test: ensure that 'percent' is a percentage.
	For example, 10 means 10% (0.10) not 10x.

	"""
	result = apply_discount(100.0, 10)
	assert result == 90.0
