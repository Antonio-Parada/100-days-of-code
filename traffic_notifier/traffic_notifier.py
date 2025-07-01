def get_traffic_info(origin, destination):
    # This is a placeholder function. In a real application,
    # you would integrate with a mapping/traffic API (e.g., Google Maps API).
    
    print(f"\nSimulating traffic information from {origin} to {destination}...")
    
    # Simulate different traffic conditions
    traffic_conditions = [
        {"route": "Main Street", "congestion": "Heavy", "eta": "30 mins"},
        {"route": "Highway 101", "congestion": "Moderate", "eta": "20 mins"},
        {"route": "Back Roads", "congestion": "Light", "eta": "25 mins"}
    ]

    print("Available Routes and Traffic:")
    for i, route in enumerate(traffic_conditions):
        print(f"{i+1}. Route: {route['route']}, Congestion: {route['congestion']}, ETA: {route['eta']}")

    # Simulate suggesting a better route
    suggested_route = traffic_conditions[1] # Suggest the moderate route
    print(f"\nSuggested Route: {suggested_route['route']} (ETA: {suggested_route['eta']}) - {suggested_route['congestion']} congestion.")

if __name__ == "__main__":
    print("--- Simple CLI Traffic Notifier Simulation ---")
    print("This script simulates traffic information and route suggestions.")
    print("It does NOT connect to real traffic data services.")

    while True:
        origin = input("\nEnter your origin (e.g., Home): ")
        destination = input("Enter your destination (e.g., Work): ")

        if origin.lower() == "exit" or destination.lower() == "exit":
            print("Exiting Traffic Notifier.")
            break

        get_traffic_info(origin, destination)
