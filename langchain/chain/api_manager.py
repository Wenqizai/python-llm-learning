from langchain_openai import ChatOpenAI
import langchain
import os

# 设置langchain的必要属性
langchain.verbose = False
langchain.debug = False
langchain.llm_cache = None

class ApiKeyManager:
    """管理API密钥和配置的类"""
    
    def __init__(self):
        self.openai_config_path = None
        self.openai_api_key = None
        self.openai_api_base_url = None
    
    def load_openai_config(self):
        """从配置文件加载API密钥和基础URL"""
        if self.openai_config_path is None:
            # 获取当前文件的目录，然后向上两级找到项目根目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            self.openai_config_path = os.path.join(project_root, "private-config", "openai-api-key")
        try:
            with open(self.openai_config_path, "r") as f:
                for line in f:
                    if line.startswith("OPENAI-API-KEY="):
                        self.openai_api_key = line.split("=", 1)[1].strip()
                    elif line.startswith("OPENAI-API-BASE-URL="):
                        self.openai_api_base_url = line.split("=", 1)[1].strip()
        except FileNotFoundError:
            print(f"警告: 配置文件 {self.openai_config_path} 未找到")
    
    def get_openai(self, model="gpt-4o-mini", temperature=0, **kwargs):
        self.load_openai_config()
        """获取配置好的ChatOpenAI实例"""
        llm_params = {"model": model, "temperature": temperature, **kwargs}
        if self.openai_api_key:
            llm_params["api_key"] = self.openai_api_key
        if self.openai_api_base_url:
            llm_params["base_url"] = self.openai_api_base_url
        
        return ChatOpenAI(**llm_params) 