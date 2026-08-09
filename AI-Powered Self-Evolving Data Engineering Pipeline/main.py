from batch_pipeline import run_batch_pipeline
from streaming_pipeline import run_streaming_pipeline

MODE = "batch"
#MODE = "stream"

if MODE == "batch":
    run_batch_pipeline()

elif MODE == "stream":
    run_streaming_pipeline()