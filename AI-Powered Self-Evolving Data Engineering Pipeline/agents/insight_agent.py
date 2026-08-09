class InsightAgent:

    def generate_insights(self, transformed_df):

        insights = []

        # Total Revenue
        total_revenue = transformed_df["revenue"].sum()

        insights.append(
            f"Total Revenue Generated: ₹{total_revenue}"
        )

        # Top Product
        top_product = (
            transformed_df.groupby("product_name")["revenue"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Top Revenue Product: {top_product}"
        )

        # Top Customer
        top_customer = (
            transformed_df.groupby("customer_name")["revenue"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Highest Value Customer: {top_customer}"
        )

        return insights