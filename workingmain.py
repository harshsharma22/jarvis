import file
def working(str):
    dict1={"hello jarvis":"hello sir how are you     MY name is jarvis           how may i help you","how are you jarvis":"i m fine sir", "what can you do for me": "anything you ask"}
    for i in dict1.keys():
        if i==str:
            f=dict1[i]
            break
        f="it is not is my data base i will update it"

    return f



