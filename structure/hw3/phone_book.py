# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))


#function: (35x+3)%10000001%100000
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [0]*10000000
    for cur_query in queries:
        hv = (35 * cur_query.number + 6) % 10000001 % 10000000
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[hv]=cur_query

        elif cur_query.type == 'del':
            contacts[hv] = 0

        else:
            response = 'not found'
            if contacts[hv]!=0:
                response=contacts[hv].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

