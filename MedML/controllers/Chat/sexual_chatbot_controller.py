from controllers.Chat.utils.session import conversation_chat

async def chatbot(query: str, chat_type: str):
    return await conversation_chat(query, chat_type)