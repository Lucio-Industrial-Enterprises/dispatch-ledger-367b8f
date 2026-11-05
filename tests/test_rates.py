import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        """Passing service='standard' must equal the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service (+$7 surcharge)
    # ------------------------------------------------------------------
    def test_express_local(self):
        # base 5 + surcharge 7 + 1.5*2 = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # base 8 + surcharge 7 + 1.5*2 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven(self):
        """Express quote must be exactly $7 more than standard for every zone."""
        for zone in ("local", "regional"):
            with self.subTest(zone=zone):
                self.assertAlmostEqual(
                    shipping_quote(5, zone, service="express"),
                    shipping_quote(5, zone, service="standard") + 7.0,
                )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
