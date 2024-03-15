import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import gradio as gr

# Load the model and tokenizer
model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Setup the pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def answer_question(context, question):
    """
    Takes a context and a question, and returns the answer based on the context.
    """
    result = nlp(question=question, context=context)
    return result['answer']

# Define the Gradio interface 
iface = gr.Interface(fn=answer_question,
                     inputs=[gr.Textbox(label="Context", placeholder="Enter the text here...", lines=7), 
                             gr.Textbox(label="Question", placeholder="Enter your question here...")],
                     outputs=gr.Textbox(label="Answer"),
                     title="Question and Answer Assistant",
                     description="Provide a context and ask a question based on that context. The assistant will find the answer for you.")

if __name__ == "__main__":
    iface.launch()
