import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return "Hello"

class RootQuery(Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
