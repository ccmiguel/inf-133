
from http.server import HTTPServer, BaseHTTPRequestHandler
import jason

class DeliveryVehicle:
    def _init_(self, capacity):
        self.capacity = capacity
        self.packages_delivered = 0
        
    def deliver(self):
        if self.packages_delivered < self.capacity:
            self.packages_delivered += 1
            return "Entrega realizada con exito"
        else: 
            return "El vehiculo ha alanzado su capacidad maxima"
        
class Motorcycle(DeliveryVehicle):
    def _init_(self):
        super()._init_(capacity=10)
        
class Drone(DeliveryVehicle):
    def _init_(self):
        super()._init_(capacity=20)
        
class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "drone":
            return Drone()
        else:
            raise ValueError("Tipo de vehiculo de entrega no encontrado")
        
class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/delivery":
            content_lenght = init(self.headers["Content-Lenght"])
            post_data = self-rfile.read(content_lenght)
            request_data = json.loads(post_data.decode("utf-8"))
            
            vehicle_type = request_data.get("vehicle_type")