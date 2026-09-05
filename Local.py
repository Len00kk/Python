from langchain_ollama import OllamaLLM
import ollama
import subprocess
# READ ME: nwm co napisac ale jak ten kod dziala: result bierze odpowiedz komputera na komende
# "ollama list" i to zapisuje, models wycina cala odp zeby tylko byly zapisane nazwy modeli,
# potem jest pętla ktora printuje kazdy model i go numeruje, zebys mogl pisac tylko numery
# a nie cale nazwy botow. odpowiedzi i prompty dzialaja w petli no i to chyba wszystko.
# credits: troche uzylam techwithtim bo on to dobrze wytlumaczyl
# time it took: mi to zajelo z godzine lub dwie, jedynie co bylo trudne to subprocess,
# bo sie na tym wgl nie znam. Ok to wszystko 
result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
output = result.stdout
print("Here are your ollama models:")
files_list = output.split('\n')
y = len(files_list)
models = [line.split()[0] for line in result.stdout.strip().split('\n')[1:] if line.strip()]
for index, model in enumerate(models, start=1):
    print(index, model)
print(f"Which model would you like to talk to? (1-{len(models)-1})")
answer = (input(""))
if answer == "/bye":
    quit()
else:
    answer = int(answer)
    answer2 = models[answer-1]
    model = OllamaLLM(model=answer2)
    print(f"Chatting with {answer2}. write '/bye' to exit.")
    while True:
        prompt = input("")
        if prompt == "/bye":
            quit()
        else:
            result = model.invoke(prompt)
            print(f"{answer2}:{result}")
            
