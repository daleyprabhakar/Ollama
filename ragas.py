# -*- coding: utf-8 -*-
"""RAGAS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dUA2R7ZCJaRrvmN6VRqHtoEHfw8WSdo6
"""

#pip install ragas datasets evaluate

from dotenv import load_dotenv
from ragas.metrics import faithfulness, answer_relevancy, context_recall, context_precision
from ragas import evaluate
from datasets import Dataset
from openai import OpenAI

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = openai_key

# Sample data from a RAG pipeline

data = {

    "question": [

        "What is the capital of France?",

        "Who is the CEO of Tesla?"

    ],

    "answer": [  # Model-generated answer

        "The capital of France is Paris.",

        "Elon Musk is the CEO of Tesla."

    ],

    "reference": [  # Ground-truth / expected answer

        "Paris is the capital of France.",

        "Elon Musk is the current CEO of Tesla."

    ],

    "contexts": [  # Retrieved chunks

        ["Paris is the capital city of France and is known for the Eiffel Tower."],

        ["Tesla is led by Elon Musk, who is also the founder of SpaceX."]

    ]

}

# Convert to HuggingFace Dataset
dataset = Dataset.from_dict(data)

# Run RAGAS Evaluation
results = evaluate(
   dataset=dataset,
   metrics=[
       faithfulness,
      answer_relevancy,
      context_precision,
      context_recall,
   ]
)

print(results)