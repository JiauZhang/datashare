import os
from datamana.core import MQueue

mq = MQueue()
mq.flags = 0
mq.msgsize = 8
mq.maxmsg = 4
errno = mq.open('/datamana', os.O_CREAT | os.O_RDWR, 600)
if errno != 0:
    print(f'MQueue open failed! <{os.strerror(errno)}>')
    exit(-1)
count = 0
pid = os.getpid()

while count < 20:
    msg = ''
    mq.receive(msg)
    print(f'<{pid}>receive msg: {msg}')
    count += 1