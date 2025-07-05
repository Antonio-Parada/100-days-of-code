class Elevator:
    def __init__(self, num_floors):
        self.current_floor = 0
        self.direction = 0  # 0: stopped, 1: up, -1: down
        self.destination_floors = []
        self.num_floors = num_floors

    def add_destination(self, floor):
        if floor not in self.destination_floors:
            self.destination_floors.append(floor)
            self.destination_floors.sort()
            if self.direction == -1: # If going down, sort in reverse
                self.destination_floors.reverse()

    def move(self):
        if not self.destination_floors:
            self.direction = 0
            return

        next_floor = self.destination_floors[0]

        if self.current_floor < next_floor:
            self.direction = 1
            self.current_floor += 1
        elif self.current_floor > next_floor:
            self.direction = -1
            self.current_floor -= 1
        else:
            # Arrived at destination
            self.destination_floors.pop(0)
            print(f"Elevator arrived at floor {self.current_floor}")
            if not self.destination_floors:
                self.direction = 0

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.has_up_request = False
        self.has_down_request = False

class Request:
    def __init__(self, start_floor, destination_floor):
        self.start_floor = start_floor
        self.destination_floor = destination_floor

class ElevatorSimulation:
    def __init__(self, num_floors, num_elevators=1):
        self.num_floors = num_floors
        self.elevators = [Elevator(num_floors) for _ in range(num_elevators)]
        self.floors = [Floor(i) for i in range(num_floors)]
        self.pending_requests = []

    def add_request(self, start_floor, destination_floor):
        request = Request(start_floor, destination_floor)
        self.pending_requests.append(request)
        if destination_floor > start_floor:
            self.floors[start_floor].has_up_request = True
        else:
            self.floors[start_floor].has_down_request = True

    def run_step(self):
        # Assign requests to elevators
        for elevator in self.elevators:
            if not elevator.destination_floors and self.pending_requests:
                # Simple assignment: take the first pending request
                request = self.pending_requests.pop(0)
                elevator.add_destination(request.start_floor)
                elevator.add_destination(request.destination_floor)
                print(f"Assigning request from {request.start_floor} to {request.destination_floor} to elevator at {elevator.current_floor}")
                
                # Clear floor request flags
                if request.destination_floor > request.start_floor:
                    self.floors[request.start_floor].has_up_request = False
                else:
                    self.floors[request.start_floor].has_down_request = False

        # Move elevators
        for elevator in self.elevators:
            elevator.move()

    def print_status(self):
        print("\n--- Elevator Status ---")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}: Floor {elevator.current_floor}, Direction {elevator.direction}, Destinations {elevator.destination_floors}")
        print("--- Floor Requests ---")
        for floor in self.floors:
            if floor.has_up_request or floor.has_down_request:
                print(f"Floor {floor.floor_number}: Up={floor.has_up_request}, Down={floor.has_down_request}")

if __name__ == "__main__":
    sim = ElevatorSimulation(num_floors=5)
    sim.add_request(2, 4)
    sim.add_request(0, 3)
    sim.add_request(4, 0)

    for _ in range(20):
        sim.run_step()
        sim.print_status()
