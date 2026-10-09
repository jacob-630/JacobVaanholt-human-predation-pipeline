from src.utils.llm_connector import get_uvic_agent

def test_system_intelligence():
    # 1. Initialize the AI Brain
    llm = get_uvic_agent()
    
    # 2. Define a research-specific prompt
    prompt = """
    You are a research assistant for a systematic review on human predation. 
    Your goal is to accurately classify data. 
    
    Analyze this text: "Over the 2023 season, 150 hunters participated. 100 successfully harvested a deer. 50 missed the shot."
    
    Extract two numbers:
    1. 'hunter_success_count' (Harvests)
    2. 'hunter_total' (Participants)
    
    Return the result as a JSON object.
    """

    print("🧠 Running UVic Qwen Agent...")
    try:
        response = llm.invoke(prompt)
        print(response.content)
        print("\n✅ Agent Intelligence Verification Complete.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_system_intelligence()
