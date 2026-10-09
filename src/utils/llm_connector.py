from langchain_openai import ChatOpenAI
from .config import AIConfig

def get_uvic_agent():
    """
    Returns a pre-configured LangChain agent connected to UVic's Qwen model.
    We set temperature=0 to ensure maximum precision and no "hallucinations" 
    during data extraction.
    """
    agent = ChatOpenAI(
        openai_api_key=AIConfig.UVIC_API_KEY,
        openai_api_base=AIConfig.UVIC_API_BASE,
        model_name=AIConfig.MODEL_NAME,
        temperature=0
    )
    return agent
