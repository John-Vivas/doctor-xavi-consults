import chainlit as cl
from semantic_kernel import Kernel
from plugins.medical_plugin import MedicalPlugin
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion


@cl.on_chat_start
async def on_chat_start():
    kernel = Kernel()

    # Integrate OpenAI service
    ai_service = OpenAIChatCompletion(
        service_id="default", ai_model_id="gpt-4o")
    kernel.add_service(ai_service)

    # Add medical plugin
    kernel.add_plugin(MedicalPlugin(), plugin_name="Medical")

    # Set up Chainlit session
    cl.user_session.set("kernel", kernel)
    cl.user_session.set("ai_service", ai_service)


@cl.on_message
async def on_message(message: cl.Message):
    kernel = cl.user_session.get("kernel")
    ai_service = cl.user_session.get("ai_service")
    chat_history = cl.user_session.get("chat_history")

    # Add user message to history
    chat_history.add_user_message(message.content)

    # Process user request (you can call any of the medical functions)
    if "diagnose" in message.content:
        response = kernel.invoke(
            "Medical.diagnose_condition", symptoms=message.content, language="en")
    elif "medicine" in message.content:
        response = kernel.invoke(
            "Medical.recommend_medicine", symptoms=message.content, language="en")
    elif "remedy" in message.content:
        response = kernel.invoke(
            "Medical.suggest_remedy", symptoms=message.content, language="en")
    elif "prevent" in message.content:
        response = kernel.invoke(
            "Medical.prevent_illness", symptoms=message.content, language="en")
    else:
        response = "Sorry, I didn't understand your request."

    # Add assistant message to history
    chat_history.add_assistant_message(response)

    # Send the final response
    await cl.Message(content=response).send()
