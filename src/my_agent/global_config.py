from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
import os


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key ,
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)
def run_global():

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model = "gemini-2.0-flash"
    )

    result = Runner.run_sync(
        agent,
        "JF-17 Thunder vs Rafael. One word answer."
    )

    print(result.final_output)
