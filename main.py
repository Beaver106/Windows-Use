# 只导入实际使用的 LLM 类，避免不必要的依赖错误
from windows_use.llms.openai import ChatOpenAI
# 其他可选模型导入（需要时取消注释并安装对应依赖）
# from windows_use.llms.google import ChatGoogle
# from windows_use.llms.anthropic import ChatAnthropic
# from windows_use.llms.ollama import ChatOllama
# from windows_use.llms.mistral import ChatMistral
# from windows_use.llms.azure_openai import ChatAzureOpenAI
# from windows_use.llms.open_router import ChatOpenRouter
# from windows_use.llms.groq import ChatGroq
from windows_use.agent import Agent, Browser
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # 使用自定义 OpenAI 兼容接口（云桥）
    llm = ChatOpenAI(
        model="claude-3-7-sonnet-20250219",  # 根据云桥平台实际模型名修改
        base_url="https://www.yunqiaoai.top/v1",
        temperature=0.7,
        # 不传 api_key 时默认从环境变量 OPENAI_API_KEY 读取
    )
    # 其他可选模型（保留原注释，方便切换）
    # llm = ChatMistral(model="magistral-small-latest", temperature=0.7)
    # llm = ChatGoogle(model="gemini-2.5-flash-lite", thinking_budget=0, temperature=0.7)
    # llm = ChatOpenRouter(model="nvidia/nemotron-3-nano-30b-a3b:free", temperature=0.2)
    # llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0.7, max_tokens=1000)
    # llm = ChatOllama(model="qwen3-vl:4b", temperature=0.2)
    # llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.7)
    agent = Agent(llm=llm, browser=Browser.EDGE, use_vision=True, use_annotation=True, auto_minimize=False, save_screenshots=True, save_screenshot_path="screenshots")
    agent.print_response(query=input("Enter a query: "))

if __name__ == "__main__":
    main()