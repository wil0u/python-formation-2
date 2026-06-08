import gradio as gr
def reverse(text):
    return text[::-1]
with gr.Blocks() as demo:
    button = gr.Button(value="Reverse")
    button.click(reverse, gr.Textbox(), gr.Textbox())
demo.launch(share=True, auth=("username", "password"))