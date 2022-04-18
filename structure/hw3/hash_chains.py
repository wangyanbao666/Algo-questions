# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [0]*bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if self.elems[query.ind]!=0:
                self.write_chain(reversed(self.elems[query.ind]))
            else:
                print('')
        else:
            try:
                ind = self._hash_func(query.s)
            except:
                ind = -1
            if query.type == 'find':
                t=-1
                # print(self.elems[ind])
                if self.elems[ind]!=0:
                    for i in self.elems[ind]:
                        if i==query.s:
                            t=1
                            break
                self.write_search_result(t != -1)
            elif query.type == 'add':
                if self.elems[ind]==0:
                    self.elems[ind]=[query.s]
                else:
                    inside=False
                    for i in self.elems[ind]:
                        if i==query.s:
                            inside=True
                            break
                    if not inside:
                        self.elems[ind].append(query.s)
            else:
                try:
                    self.elems[ind].remove(query.s)
                except:
                    pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


# add test
# add test
# find test
# del test
# find test
# find Test
# add Test
# find Test