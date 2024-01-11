

# --------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           Generar guiones mediante LLM (GPT 2 Medium, de openAI, disponible solo en inglés):
# --------------------------------------------------------------------------------------------------------------------------------------------------------

from transformers import pipeline

titulo = input("Write the main theme or a title for your video: ")


pipe = pipeline("text-generation", model="gpt2-medium") # Este modelo de LLM solo genera texto en inglés :(
max_length = 100  
num_return_sequences = 1

generated_text = pipe (
        f"Write the content of a video, with the title: {titulo}",
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,  
        pad_token_id=50256,  # Identificador de token de relleno para GPT-2
    )
print(generated_text)



