
#
#序列号发生器服务端实现(pb 风格)
#

import grpc
import logging
from threading import Lock
from gs.pb import seqence_pb2_grpc
from gs.pb.seqence_pb2 import SeqenceID

class SeqenceDaemo(seqence_pb2_grpc.SeqenceServicer):
    _global_id = 0
    _lock = Lock()
    def get_id(self, request, context):
        """
        """
        logging.info(f"{request.client_name} want a new id.")
        with self._lock:
            self._global_id = self._global_id + 1
            logging.info(f"we assign it {self._global_id - 1}")
            return SeqenceID(id=self._global_id - 1) 
