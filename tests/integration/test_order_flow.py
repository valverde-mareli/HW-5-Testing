from order_io import load_order, write_receipt

def test_order_integration(tmp_path):
	input_file = tmp_path / "order.csv"
	input_file.write_text(
		"widget,$10.00\n"
		"gizmo,5.50\n",
		encoding="utf-8"
	)

	items = load_order(input_file)
	assert items == [("widget", 10.0), ("gizmo", 5.5)]

	receipt_file = tmp_path / "receipt.txt"
	write_receipt(receipt_file, items, discount_percent=10, tax_rate=0.10)

	output = receipt_file.read_text(encoding="utf-8")
	assert "widget: $10.00" in output
	assert "gizmo: $5.50" in output
	assert "TOTAL:" in output
