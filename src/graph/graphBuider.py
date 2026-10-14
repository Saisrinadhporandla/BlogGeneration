from langgraph.graph import StateGraph,START,END
from src.graph.stateCre import State
from src.graph.nodeCre import Nodes
from src.LLMs.LLM import ModelClass
class classGraph():
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(State)

    def buildGraph(self):
        node=Nodes(self.llm)
        graph=self.graph
        graph.add_node("title_creation",node.titleNode)
        graph.add_node("content_creation",node.contentNode)
        graph.add_edge(START,"title_creation")
        graph.add_edge("title_creation","content_creation")
        graph.add_edge("content_creation",END)
        return graph.compile()
llm=ModelClass().load_llm()
graph_builder=classGraph(llm)
graph=graph_builder.buildGraph()
        