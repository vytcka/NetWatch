class IpRecord :
    def __init__(self, src_ip, dst_ip, protocol, timestamp, dst_port):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.timestamp = timestamp
        self.dst_port = dst_port
        
        #no need for getters, implomentation will be needed to be added later;
    def retrieve_connections(self, file : str, list : list) -> object:
        f = open(file)
        for line in f:
            
        
    def retrieve_source(self, IpRecord)->str:
        
        