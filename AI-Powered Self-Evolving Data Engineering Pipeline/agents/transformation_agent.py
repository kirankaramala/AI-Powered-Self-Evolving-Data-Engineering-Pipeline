class TransformationAgent:

    def transform(self, datasets):

        orders = datasets["orders"]
        customers = datasets["customers"]
        products = datasets["products"]

        transformed_df = (
            orders
            .merge(customers, on="customer_id", how="left")
            .merge(products, on="product_id", how="left")
        )

        transformed_df["revenue"] = (
            transformed_df["quantity"]
            * transformed_df["price"]
        )

        return transformed_df