# -*- coding: utf-8 -*-


# huggingface code-bert model and tokenizer
# no need to run

from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("codistai/codeBERT-small-v2")

model = AutoModelWithLMHead.from_pretrained("codistai/codeBERT-small-v2")
