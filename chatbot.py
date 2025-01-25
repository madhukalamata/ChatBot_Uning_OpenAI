from openai import OpenAI
import gradio

OpenAI.api_key = " (Create API) "

messages = [{"role": "system", "content": "You are an AI that provides answers to questions asked "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = OpenAI.ChatCompletion.create(
        model = "gpt-4o-mini",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Madhu_GPT")

demo.launch(share=True)
