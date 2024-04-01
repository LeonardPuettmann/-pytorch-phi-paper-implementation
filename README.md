In this repo, we train a nano version of Microsofts Phi-2 model. 

## Motivation
Phi-2 is a phenomenal model, with just `2.7 Billion parameters` and > 4 GB in full precision it can indeed be consideres a tiny model compared to
models like GPT-4 or even open-source models like the 70B LLaMA 2. Despite it's small size, the model was trained on 1.4T tokens, which is massive compared to the 400B tokens that were reportedly used to train GPT-3 at 175B parameters.

With that in mind, we can assume two things: 
- a) That language models can be made much smaller and still produce good results. 
- b) The data quality is the most important factor in building good models, and vasts amounts of high quality data allow you to decrease the model size. 

This made me very curious to understand more about this and try if I can replicate this myself. Therefore, this repository trackles the following topics: 
- How can we use an ML approach to filter out high quality parts from already existing datasets. 
- Using GPT models, especially the cheaper GPT-3.5-turbo, to generate hight quality synthetic datases with `textbook quality`.
- Replicating Phi-2 with PyTroch.

You can read more about Phi-2 here: https://huggingface.co/microsoft/phi-2

## Findings and results 

Dataset: 
more soon.

Model: 
Because I am relatively GPU poor and don't have any A100 GPUs (let alone 8 of them like the authors had), the replicated model is `much smaller and much simpler` than the Phi-2 model. The `Phi-2-supernano` rocks only about 7 Million parameters, more similar to the `TinyStories` models which are around the 10M mark. Please note that `Phi-2-supernano` is not very useful for anything, really.

## Links and futher reading:
Original papers for Phi-1 and Phi-1.5
- `Textbooks Are All You Need`: https://arxiv.org/abs/2306.11644
- `Textbooks Are All You Need II: phi-1.5 technical report`: https://arxiv.org/abs/2309.05463

Similar paper for small LLMs:
- `TinyStories: How Small Can Language Models Be and Still Speak Coherent English?`: https://arxiv.org/abs/2305.07759

### Achknowledgement
This repository is for educational purposes! All credit goes to the respected authors and publishers of the papers and original models. 