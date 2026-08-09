import pandas as pd


class QualityAgent:

    def check_quality(
        self,
        orders,
        customers,
        products
    ):

        report = {}

        # -----------------------------
        # Orders Dataset Checks
        # -----------------------------

        missing_values = orders.isnull().sum().sum()

        duplicate_rows = orders.duplicated().sum()

        # Date Validation
        invalid_dates = pd.to_datetime(
            orders["order_date"],
            errors="coerce"
        ).isna().sum()

        # Numeric Validation
        invalid_price = pd.to_numeric(
            orders["price"],
            errors="coerce"
        ).isna().sum()

        invalid_quantity = pd.to_numeric(
            orders["quantity"],
            errors="coerce"
        ).isna().sum()

        # Negative Values
        negative_price = (
            pd.to_numeric(
                orders["price"],
                errors="coerce"
            ) < 0
        ).sum()

        negative_quantity = (
            pd.to_numeric(
                orders["quantity"],
                errors="coerce"
            ) < 0
        ).sum()

        # Customer Integrity
        invalid_customers = (
            ~orders["customer_id"].isin(
                customers["customer_id"]
            )
        ).sum()

        # Product Integrity
        invalid_products = (
            ~orders["product_id"].isin(
                products["product_id"]
            )
        ).sum()

        total_issues = (
            missing_values
            + duplicate_rows
            + invalid_dates
            + invalid_price
            + invalid_quantity
            + negative_price
            + negative_quantity
            + invalid_customers
            + invalid_products
        )

        total_rows = len(orders)

        quality_score = max(
            0,
            round(
                (
                    (total_rows - total_issues)
                    / total_rows
                ) * 100,
                2
            )
        )

        report["orders"] = {
            "Missing Values": int(missing_values),
            "Duplicate Rows": int(duplicate_rows),
            "Invalid Dates": int(invalid_dates),
            "Invalid Prices": int(invalid_price),
            "Invalid Quantities": int(invalid_quantity),
            "Negative Prices": int(negative_price),
            "Negative Quantities": int(
                negative_quantity
            ),
            "Invalid Customers": int(
                invalid_customers
            ),
            "Invalid Products": int(
                invalid_products
            ),
            "Quality Score": quality_score
        }

        return report

    def print_report(self, report):

        print(
            "\n========== QUALITY REPORT ==========\n"
        )

        for dataset, metrics in report.items():

            print(f"\nDataset : {dataset}")

            for key, value in metrics.items():

                print(
                    f"{key} : {value}"
                )