from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": 
            {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            },
            "weather": 
            {
                "url":"http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") # this I have add my API key in .env file where you have to create by yourself
    
    tools = await client.get_tools()
    model = ChatGroq(model="moonshotai/kimi-k2-instruct")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages" : [{"role": "user", "content": "What is (10 + 20) x 30?"}]}
    )

    print("Math Response: ", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages" : {"role": "user", "content": "what is the weather in Delhi?"} }
    )

    print("Weather Response: ", weather_response['messages'][-1].content)

asyncio.run(main())
