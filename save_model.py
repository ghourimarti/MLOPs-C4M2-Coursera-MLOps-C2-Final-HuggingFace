"""
After running zip it to save
zip -r summarizeApp.zip summarizeApp 
"""
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
from transformers import pipeline

model = pipeline(
    "summarization",
    #model="sshleifer/distilbart-cnn-12-6",
    model="google-t5/t5-small",
    #revision="a4f8f3e",
    from_pt=True  # 🔑 This tells it to load PyTorch weights
)
model.save_pretrained("summarizeApp")