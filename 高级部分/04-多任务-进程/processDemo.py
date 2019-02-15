from multiprocessing import Process, Queue


def que1(q):
    print(q)
    print(q.empty())


if __name__ == '__main__':
    q = Queue()
    ps1 = Process(target=que1, args=(q,))
    ps1.start()
