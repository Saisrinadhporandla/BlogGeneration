from fastapi import FastAPI,Request
from src.graph.graphBuider import classGraph
from src.LLMs.LLM import ModelClass

app=FastAPI()

@app.get("/health")
def checkStatus():
    return {"status":"okay"}

@app.post("/blog")
async def createBlog(request:Request):
    data=await request.json()
    topic=data.get("topic")
    model=ModelClass().load_llm()
    graph=classGraph(model).buildGraph()
    result=graph.invoke({"topic":topic})
    return {"data":result}
