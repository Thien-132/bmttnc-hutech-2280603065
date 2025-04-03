import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()
    
    def open(self):
        WebSocketServer.clients.add(self)
        
    def on_close(self):
        WebSocketServer.clients.remove(self)
        
    def send_message(cls, message: str):
        print()