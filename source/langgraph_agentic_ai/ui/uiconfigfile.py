from configparser import ConfigParser

class Config: 
    def __init__(self,config_file= "./source/langgraph_agent_ai/ui/uiconfigfile.ini"):
        self.congif= ConfigParser
        self.congif.read(config_file)
    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")