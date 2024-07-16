
import gradio as gr
from backend_test import main as chat_bot

css = """
h1 {
    text-align: center;
    display:block;
}
"""


# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)


mytheme = gr.themes.Soft(
    primary_hue="orange",
    secondary_hue="amber",
    spacing_size="sm",
    radius_size="lg",
).set(
    block_background_fill='*primary_300',
    block_background_fill_dark='*primary_100',
    input_background_fill='*primary_100',
)

gr.ChatInterface(
    chat_bot,
    chatbot=gr.Chatbot(height=600),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Chatbot",
    description="Hangman game",
    theme=mytheme,
    examples=["Hello", "What's up", "How was your weekend"],
    cache_examples=False,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()


