from google.generativeai import list_models
import google.generativeai as genai

genai.configure(api_key="ypur_api_key")
models = list_models()

for model in models:
    print(model.name, model.supported_generation_methods)
