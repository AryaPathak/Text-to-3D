from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class LocalLLM:
    def __init__(self, model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        print("Loading local LLM...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if torch.cuda.is_available() else -1
        )

    def expand_prompt(self, prompt: str) -> str:
        prompt_template = f"Expand this into a detailed visual scene description:\n\n{prompt}\n\nExpanded:"
        outputs = self.generator(prompt_template, max_length=200, do_sample=True, temperature=0.7)
        raw_output = outputs[0]['generated_text']
        print("\n--- Raw LLM Output ---\n")
        print(raw_output)
        print("\n--- Extracted Expansion ---\n")
        print(raw_output.split("Expanded:")[-1].strip())
        return raw_output.split("Expanded:")[-1].strip()
