from streaming.consumer import consume_stream

from agents.quality_agent import QualityAgent
from agents.transformation_agent import TransformationAgent
from agents.insight_agent import InsightAgent
from agents.ai_insight_agent import AIInsightAgent
from agents.human_feedback_agent import HumanFeedbackAgent
from agents.learning_agent import LearningAgent

import pandas as pd
import json
import sys


def run_streaming_pipeline():

    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")

    quality_agent = QualityAgent()
    transformation_agent = TransformationAgent()
    insight_agent = InsightAgent()
    ai_insight_agent = AIInsightAgent()
    feedback_agent = HumanFeedbackAgent()
    learning_agent = LearningAgent()

    for orders in consume_stream():

        print("=" * 50)

        # Quality
        quality_report = quality_agent.check_quality(
            orders,
            customers,
            products
        )

        quality_agent.print_report(quality_report)
        
        score = quality_report["orders"]["Quality Score"]
        if score  < 95:
            print(
                f"""
                CRITICAL ERROR

                Quality Threshold Breached

                Expected: >=95
                Actual: {score}

                Pipeline Terminated
                """
            )   
            sys.exit(1)
        print("\n========== TRANSFORMED DATA ==========\n")
        # Transformation
        #transformed_data = transformation_agent.transform(
        #    orders,
        #    customers,
        #    products
        #)
        feedback = pd.read_csv("data/feedback.csv")
        data = {
            "orders": orders,
            "customers": customers,
            "products": products,
            "feedback": feedback
        }
        transformed_data = transformation_agent.transform(data)
        print(transformed_data)
        insights = insight_agent.generate_insights(transformed_data)

        print("\n========== INSIGHTS ==========\n")

        for insight in insights:
            print("-", insight)
        with open("outputs/insights.txt", "w", encoding="utf-8") as f:
            for insight in insights:
                f.write(insight + "\n")
    
        feedback_records = feedback_agent.process_feedback(data["feedback"])

        feedback_agent.save_feedback(feedback_records)
    
        total_revenue = transformed_data["revenue"].sum()
    
        print("\n========== ACTIVE RULES ==========\n")
        with open(
            "memory/rules.json",
            "r",
            encoding="utf-8"
        ) as f:

            rules = json.load(f)
        print(rules)

        print("\n========== AI INSIGHTS ==========\n")
        top_product = (
            transformed_data.groupby(
                "product_name"
                )["revenue"]
                .sum().
                idxmax()
        )

        top_customer = (
            transformed_data.groupby(
                "customer_name"
                )["revenue"]
                .sum()
                .idxmax()
        )

        ai_response = (
            ai_insight_agent.generate_ai_insights(
            total_revenue,
            top_product,
            top_customer
            )
        )
        print(ai_response)

        print("\n========== HUMAN FEEDBACK ==========\n")

        for record in feedback_records:

            print(f"Insight : {record['insight']}")

            print(f"Status : {record['status']}")

            print(f"Correction : {record['correction']}")

            print("-" * 40)
        
        
        learning_recommendations = (learning_agent.learn_from_feedback(feedback_records))

        print("\n========== AI POWERED LEARNING AGENT ==========\n")

        learning_output = (
            learning_agent.learn_from_feedback(
                feedback_records
            )
        )

        print(learning_output)

        updated_rules = (
            learning_agent.update_rules()
        )

        print("\n========== UPDATED RULES ==========\n")
        print(updated_rules)
    
    

    if __name__ == "__main__":
        run_streaming_pipeline()

        # TODO
        # Transformation

        # TODO
        # Insights

        # TODO
        # AI

        # TODO
        # Feedback

        # TODO
        # Learning