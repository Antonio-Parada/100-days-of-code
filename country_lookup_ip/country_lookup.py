import requests
import sys

def get_country_from_ip(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        if data and data['status'] == 'success':
            country = data.get('country')
            city = data.get('city')
            region_name = data.get('regionName')
            
            print(f"IP Address: {ip_address}")
            print(f"Country: {country}")
            if city and region_name:
                print(f"Location: {city}, {region_name}")
            elif city:
                print(f"Location: {city}")
            elif region_name:
                print(f"Location: {region_name}")
        else:
            print(f"Could not retrieve information for IP: {ip_address}. Status: {data.get('status')}, Message: {data.get('message')}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to IP geolocation service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python country_lookup.py <IP_ADDRESS>")
        sys.exit(1)

    ip_to_lookup = sys.argv[1]
    get_country_from_ip(ip_to_lookup)
