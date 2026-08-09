# AI-Powered Self-Evolving Data Engineering Pipeline
### Capstone Project – AI in Modern Data Engineering

## Project Overview

This project demonstrates an AI-powered modern data engineering pipeline capable of processing both **Batch** and **Real-Time Streaming** data.

Unlike traditional ETL pipelines, this solution incorporates multiple AI agents that continuously validate data quality, generate business insights, accept human feedback, and improve future recommendations through a learning mechanism.

The project showcases how Agentic AI can augment Data Engineering by enabling intelligent, self-improving data pipelines.

---

#How to run the project
	1. main.py consists the choice between batch mode and streaming mode
	2. select the mode inside the main.py before running it by uncommenting the desired option . "#MODE = "stream"" means main.py will execute batch pipeline
	3. Batch pipeline will execute without any input for data ingestion
	4. If we need to run only batch pipeline, run batch_pipeline.py . If only streaming pipeline needs to be run, run streaming_pipeline.py 
	4. 	```bash
		python main.py
		```

	### Batch Mode

	- Reads input data from CSV files located in the `data/` folder.
	- Executes the complete AI-powered data pipeline.
	- No additional setup or input is required after execution.

	### Streaming Mode

	Before running the streaming pipeline:

	1. Start the Kafka ecosystem using Docker Compose.
	2. Ensure MySQL, Debezium, Kafka, and Kafka Connect are running.
	3. Run `python main.py`.
	4. Insert a new record into the `orders_stream` table in MySQL.

	Example:

	```sql
	INSERT INTO orders_stream VALUES (1007,'C001','P001',2,1200,'2026-06-28');
	```

	The newly inserted record will automatically flow through:

	- Debezium CDC
	- Kafka
	- Streaming Consumer
	- Quality Agent and other agents which are common both in batcha and streaming pipelines. 

# Key Features

✅ Batch Data Processing (CSV)

✅ Real-Time Streaming using Kafka + Debezium + MySQL CDC

✅ Automated Data Quality Validation

✅ Intelligent Data Transformation

✅ Business Insight Generation

✅ AI-powered Business Recommendations (LLM - Ollama)

✅ Human-in-the-loop Feedback

✅ Learning Agent for Continuous Improvement

✅ Dynamic Business Rules

---

# Architecture

                    Batch Pipeline

              CSV Files
                   │
                   ▼
            Ingestion Agent
                   │
                   ▼
             Quality Agent
                   │
                   ▼
         Transformation Agent
                   │
                   ▼
            Insight Agent
                   │
                   ▼
          AI Insight Agent
                   │
                   ▼
       Human Feedback Agent
                   │
                   ▼
           Learning Agent

------------------------------------------------------------

                 Streaming Pipeline

 MySQL
    │
    ▼
Debezium CDC
    │
    ▼
 Kafka Topic
    │
    ▼
 Kafka Consumer
    │
    ▼
 Parser
    │
    ▼
 Quality Agent
    │
    ▼
 Transformation Agent
    │
    ▼
 Insight Agent
    │
    ▼
 AI Insight Agent
    │
    ▼
 Human Feedback Agent
    │
    ▼
 Learning Agent

---

# Project Folder Structure

```
Capstone_Project_06/

│
├── agents/
│   ├── ingestion_agent.py
│   ├── quality_agent.py
│   ├── transformation_agent.py
│   ├── insight_agent.py
│   ├── ai_insight_agent.py
│   ├── human_feedback_agent.py
│   └── learning_agent.py
│
├── data/
│   ├── orders.csv
│   ├── customers.csv
│   ├── products.csv
│   └── feedback.csv
│
├── docs/
│   ├── architecture.png
│   ├── batch_output.txt
│   ├── streaming_output.txt
│   └── screenshots/
│  		 ├── batch_execution.png
│  		 ├── kafka_ui.png
│  		 ├── mysql_table.png
│  		 ├── streaming_execution.png
│  		 
├── streaming/
│   ├── consumer.py
│   └── parser.py
│
├── memory/
│   └── rules.json
│
├── outputs/
│
├── batch_pipeline.py
├── streaming_pipeline.py
├── main.py
│
└── README.md
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Pipeline |
| Pandas | Data Processing |
| Kafka | Event Streaming |
| Debezium | Change Data Capture |
| MySQL | Source Database |
| Docker | Containerization |
| Kafka UI | Topic Monitoring |
| Ollama | Local LLM |
| JSON | Business Rules |
| CSV | Batch Data Source |

---

# AI Agents

## 1. Ingestion Agent

Responsible for loading batch datasets.

Input:
- Orders
- Customers
- Products
- Feedback

Output:
Unified data dictionary.

---

## 2. Quality Agent

Performs automated validation checks.

Checks include:

- Missing Values
- Duplicate Records
- Invalid Dates
- Invalid Prices
- Negative Quantities
- Invalid Customers
- Invalid Products

Generates a Quality Score.

Critical failures terminate the batch pipeline.

Streaming mode skips invalid events while continuing to process subsequent events.

---

## 3. Transformation Agent

Responsible for

- Joining datasets
- Revenue calculation
- Business-ready dataset creation

Output:

Transformed analytical dataset.

---

## 4. Insight Agent

Generates KPIs including:

- Total Revenue
- Top Revenue Product
- Highest Value Customer

---

## 5. AI Insight Agent

Uses Ollama LLM to generate

- Business Insights
- Risks
- Recommendations

Prompt is dynamically constructed using

- Business Rules
- Pipeline Outputs
- KPI Results

---

## 6. Human Feedback Agent

Allows domain experts to validate AI-generated insights.

Feedback includes

- Correct
- Incorrect
- Suggested Correction

---

## 7. Learning Agent

Analyzes feedback and recommends

- Business Rule Updates
- Prompt Improvements
- Expected Model Enhancements

The updated rules are stored in

```
memory/rules.json
```

---

# Batch Pipeline Execution

Run

```
python batch_pipeline.py
```

Workflow

```
CSV
 ↓
Quality Validation
 ↓
Transformation
 ↓
Insights
 ↓
AI Insights
 ↓
Human Feedback
 ↓
Learning Agent
```

---

# Streaming Pipeline Execution

Start Kafka ecosystem

```
docker compose up -d
```

Run Streaming Pipeline

```
python main.py
```

(or `python main.py stream` if using command-line mode)

Workflow

```
MySQL Insert

↓

Debezium CDC

↓

Kafka Topic

↓

Kafka Consumer

↓

Parser

↓

Quality Validation

↓

Transformation

↓

Insights

↓

AI Insights

↓

Learning Agent
```

Every newly inserted record is automatically processed.

---

# Sample Streaming Event

```
INSERT INTO orders_stream
VALUES(
1007,
'C001',
'P001',
2,
1200,
'2026-06-28'
);
```

The pipeline immediately generates

- Quality Report
- Transformed Dataset
- Business Insights
- AI Recommendations
- Learning Suggestions

without restarting the application.

---

# Business Rules

Business rules are stored in

```
memory/rules.json
```

Example

```json
{
    "sales_drop_threshold": 10,
    "quality_threshold": 95,
    "seasonality_check": true
}
```

These rules are referenced by the AI Insight Agent while generating recommendations.

---

# Future Enhancements

- Historical trend analysis
- Dynamic prompt optimization
- Automatic business rule updates
- Airflow orchestration
- Cloud deployment
- Spark Structured Streaming
- Dashboard using Grafana/Power BI
- Multi-LLM support
- Agent memory optimization
- Vector Database integration

---

# Key Learning Outcomes

This project demonstrates

- Modern Data Engineering
- Batch Processing
- Streaming Data Processing
- Change Data Capture
- Kafka Integration
- Data Quality Engineering
- AI-assisted Analytics
- Human-in-the-loop AI
- Agentic AI
- Self-improving Data Pipelines

---

# Author

**Kiran Kumar**

Capstone Project

AI in Modern Data Engineering

2026
