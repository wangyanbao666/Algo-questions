# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [0]
        self.has=1

    def process(self, request):
        # write your code here
        if request.arrived_at<self.finish_time[-1]:
            # print('t')
            self.has+=1
            if self.size<len(self.finish_time):
                if request.arrived_at >= self.finish_time[-self.size]:
                    self.has -= 1
        if self.has>self.size:
            self.has-=1
            return Response(True, -1)
        else:
            start_time = max(self.finish_time[-1], request.arrived_at)
            self.finish_time.append(start_time + request.time_to_process)
            return Response(False,start_time)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
        # print('has:', buffer.has)
    # print(buffer.finish_time)
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

# 2 4
# 1 3
# 2 3
# 3 3
# 6 1

if __name__ == "__main__":
    main()
