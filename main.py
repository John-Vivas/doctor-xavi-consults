import chainlit as cl
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from contents.chat_history import ChatHistory

from plugins.medical_plugin import MedicalPlugin
from services.translation_service import TranslationService

translator = TranslationService()


@cl.on_chat_start
async def on_chat_start():
    kernel = Kernel()

    ai_service = OpenAIChatCompletion(
        service_id="default", ai_model_id="gpt-4o")
    kernel.add_service(ai_service)

    # Añadir el plugin correctamente al Kernel
    medical_plugin = MedicalPlugin()
    kernel.add_plugin(medical_plugin, plugin_name="Medical")

    cl.user_session.set("kernel", kernel)
    cl.user_session.set("ai_service", ai_service)
    cl.user_session.set("chat_history", ChatHistory())


@cl.on_message
async def on_message(message: cl.Message):
    kernel = cl.user_session.get("kernel")
    ai_service = cl.user_session.get("ai_service")
    chat_history = cl.user_session.get("chat_history")

    # Detectar idioma original del usuario
    user_lang = translator.detect_language(message.content)

    # Traducir a inglés
    translated_input = translator.to_english(message.content)
    print(f"Translated Input: {translated_input}")  # Agregar esto para depurar
    chat_history.add_user_message(translated_input)

    # Elegir función médica según el texto traducido
    if "diagnose" in translated_input:
        # Usar el nombre completamente cualificado de la función registrada en el Kernel
        print("Triggering diagnose_condition")
        response = await kernel.invoke(
            "Medical.diagnose_condition", symptoms=translated_input, language="en"
        )
    elif "medicine" in translated_input:
        response = await kernel.invoke(
            "Medical.recommend_medicine", symptoms=translated_input, language="en"
        )
    elif "remedy" in translated_input:
        response = await kernel.invoke(
            "Medical.suggest_remedy", symptoms=translated_input, language="en"
        )
    elif "prevent" in translated_input:
        response = await kernel.invoke(
            "Medical.prevent_illness", symptoms=translated_input, language="en"
        )
    else:
        response = "Sorry, I didn't understand your request."

    # Traducir respuesta al idioma original
    final_response = translator.to_original_language(response, user_lang)
    chat_history.add_assistant_message(final_response)

    await cl.Message(content=final_response).send()
