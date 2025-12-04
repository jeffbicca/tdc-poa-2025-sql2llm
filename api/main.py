from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from toolbox_langchain import ToolboxClient

from uvicorn.main import main

import sys

model = ChatOpenAI(openai_api_key="SUA_OPENAI_API_KEY")
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat_with_gpt(request: PromptRequest):
    try:
        async with ToolboxClient("http://127.0.0.1:5000") as client:
            tools = await client.aload_toolset()

            agent = create_react_agent(model, tools, checkpointer=MemorySaver())

            config = {"configurable": {"thread_id": "thread-1"}}
            inputs = {"messages": [("user", request.prompt)]}
            response = agent.invoke(inputs, stream_mode="values", config=config)
            response = response["messages"][-1].content
            return {"response": response}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    sys.exit(main())