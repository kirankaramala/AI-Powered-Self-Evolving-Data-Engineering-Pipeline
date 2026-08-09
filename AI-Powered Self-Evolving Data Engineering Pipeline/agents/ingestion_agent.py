import pandas as pd

class IngestionAgent:

    def load_data(self):

        orders = pd.read_csv("data/orders.csv")
        customers = pd.read_csv("data/customers.csv")
        products = pd.read_csv("data/products.csv")
        feedback = pd.read_csv("data/feedback.csv")

        return {
            "orders": orders,
            "customers": customers,
            "products": products,
            "feedback": feedback
        }