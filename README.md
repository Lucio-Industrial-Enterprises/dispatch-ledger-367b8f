# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter | Values | Notes |
|-----------|--------|-------|
| `weight_kg` | positive float | Parcel weight |
| `zone` | `local`, `regional` | Delivery zone |
| `service` | `standard` *(default)*, `express` | Express adds a flat $7 surcharge |

Unknown zones or service levels raise `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                    # $8.00  (standard)
python -m warehouse.cli 2 local --service express  # $15.00 (express)
python -m warehouse.cli 2 regional                 # $11.00 (standard)
```
