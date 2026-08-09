import json


class HumanFeedbackAgent:

    def process_feedback(self, feedback_df):

        feedback_records = []

        for _, row in feedback_df.iterrows():

            feedback_records.append(
                {
                    "insight": row["insight"],
                    "status": row["status"],
                    "correction": row["correction"]
                }
            )

        return feedback_records

    def save_feedback(self, feedback_records):

        with open(
            "memory/feedback_memory.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                feedback_records,
                f,
                indent=4
            )