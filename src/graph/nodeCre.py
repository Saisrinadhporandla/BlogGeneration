from src.graph.stateCre import State

class Nodes():
    def __init__(self,llm):
        self.llm=llm
    def titleNode(self,state:State):
        prompt="""
        you are an expert blog title writer. Generate exactly ONE title for a blog about {topic}
            """
        systemMsg= prompt.format(topic=state["topic"])
        response= self.llm.invoke(systemMsg)
        return {"blog":{"title":response.content}}

    def contentNode(self,state:State):
        prompt="""
     You are an expert content writer. write content for the topic {topic}, Return the article in Markdown format.
        """
        systemMsg= prompt.format(topic=state["topic"])
        response=self.llm.invoke(systemMsg)
        return {"blog":{"title":state["blog"]["title"],"content":response.content}}

