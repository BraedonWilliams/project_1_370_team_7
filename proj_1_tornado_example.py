import tornado.ioloop  # Import Tornado's I/O loop for managing asynchronous events
import tornado.web     # Import Tornado's web framework for handling HTTP requests
import tornado.websocket  # Import Tornado's WebSocket support for real-time communication

# Define a request handler for the root URL
# This class handles GET requests to the root URL ("/")
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Respond with a simple message when the root URL is accessed
        self.write("Welcome to Tornado!")

# Define a request handler for POST requests
# This class handles POST requests to the "/submit" URL
class SubmitHandler(tornado.web.RequestHandler):
    def post(self):
        # Retrieve data from the POST request body
        data = self.get_body_argument("data", default="No data provided")
        # Respond with the received data
        self.write(f"Received data: {data}")

# Define a WebSocket handler for real-time communication
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        # Called when a new WebSocket connection is opened
        print("WebSocket connection opened")
        self.write_message("Welcome to the WebSocket!")

    def on_message(self, message):
        # Called when a message is received from the client
        print(f"Received message: {message}")
        self.write_message(f"Echo: {message}")

    def on_close(self):
        # Called when the WebSocket connection is closed
        print("WebSocket connection closed")

# Function to create the Tornado application
# This function maps URLs to their respective request handlers
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),  # Map the root URL ("/") to the MainHandler class
        (r"/submit", SubmitHandler),  # Map the "/submit" URL to the SubmitHandler class
        (r"/websocket", WebSocketHandler),  # Map the "/websocket" URL to the WebSocketHandler class
    ])

# Entry point of the application
if __name__ == "__main__":
    app = make_app()  # Create the Tornado application
    app.listen(8888)  # Start the server and listen on port 8888
    print("Tornado server is running on http://localhost:8888")  # Inform the user that the server is running
    print("WebSocket endpoint available at ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()  # Start the Tornado I/O loop to handle incoming requests