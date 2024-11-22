import tkinter as tk
from tkinter import ttk, scrolledtext
import numpy as np
import random
# Distance matrix (in km) between places
places = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Jaipur", 
    "Agra", "Gwalior", "Varanasi", "Lucknow", "Amritsar", 
    "Hyderabad", "Pune", "Coimbatore", "Mysore", "Bhopal"
]
opt=["Nature","Culture","History"]
distances = np.array([
    [0, 1400, 1500, 2200, 280, 233, 320, 815, 554, 450, 1250, 1460, 2410, 2100, 760],  # Delhi
    [1400, 0, 2050, 1330, 1170, 1217, 1517, 1430, 1360, 1600, 710, 150, 1200, 1030, 800],  # Mumbai
    [1500, 2050, 0, 1660, 1530, 1250, 1370, 670, 985, 1910, 1450, 2020, 2100, 1860, 1120],  # Kolkata
    [2200, 1330, 1660, 0, 2180, 2550, 2710, 2350, 2110, 2650, 630, 930, 490, 380, 1140],  # Chennai
    [280, 1170, 1530, 2180, 0, 240, 360, 920, 610, 600, 1450, 1350, 2380, 2050, 580],  # Jaipur
    [233, 1217, 1250, 2550, 240, 0, 120, 800, 580, 470, 1300, 1420, 2460, 2150, 540],  # Agra
    [320, 1517, 1370, 2710, 360, 120, 0, 850, 610, 520, 1400, 1550, 2600, 2300, 600],  # Gwalior
    [815, 1430, 670, 2350, 920, 800, 850, 0, 330, 1130, 1340, 1550, 2300, 2000, 820],  # Varanasi
    [554, 1360, 985, 2110, 610, 580, 610, 330, 0, 900, 1260, 1460, 2200, 1900, 680],  # Lucknow
    [450, 1600, 1910, 2650, 600, 470, 520, 1130, 900, 0, 1750, 1550, 2600, 2300, 920],  # Amritsar
    [1250, 710, 1450, 630, 1450, 1300, 1400, 1340, 1260, 1750, 0, 550, 450, 360, 720],  # Hyderabad
    [1460, 150, 2020, 930, 1350, 1420, 1550, 1550, 1460, 1550, 550, 0, 1010, 860, 900],  # Pune
    [2410, 1200, 2100, 490, 2380, 2460, 2600, 2300, 2200, 2600, 450, 1010, 0, 300, 980],  # Coimbatore
    [2100, 1030, 1860, 380, 2050, 2150, 2300, 2000, 1900, 2300, 360, 860, 300, 0, 850],  # Mysore
    [760, 800, 1120, 1140, 580, 540, 600, 820, 680, 920, 720, 900, 980, 850, 0]   # Bhopal
])

# Attractions for each place
# Grouped attractions for all places by type
attractions = {
    "Delhi": {
        "history": [("Red Fort", 5), ("Qutub Minar", 18.5), ("Jama Masjid", 17.2)],
        "nature": [("Lodhi Garden", 5), ("Yamuna Biodiversity Park", 20.9), ("Garden of Five Senses", 32.8)],
        "culture": [("India Gate", 7.7), ("Humayun's Tomb", 3.7), ("Dilli Haat", 6.8)],
        
    },
    "Mumbai": {
        "nature": [("Sanjay Gandhi National Park", 20), ("Juhu Beach", 21), ("Marine Drive", 22)],
        "culture": [("Gateway of India", 4), ("Elephanta Caves", 20), ("Prince of Wales Museum", 1.4)],
        "history": [("Chhatrapati Shivaji Terminus", 5), ("Kanheri Caves", 45), ("Mani Bhavan", 42)],
    },
    "Kolkata": {
        "nature": [("Eco Park", 13.2), ("Howrah Bridge", 18.1), ("Botanical Gardens", 6.7)],
        "culture": [("Victoria Memorial", 6), ("Dakshineswar Temple", 16,9), ("Kalighat Temple", 30.3)],
        "history": [("Indian Museum", 8), ("Marble Palace", 3.7), ("Jorasanko Thakur Bari",1 )],
    },
    "Chennai": {
        "nature": [("Marina Beach", 4.6), ("Elliot's Beach", 27.0), ("Guindy National Park", 22.5)],
        "culture": [("Kapaleeshwarar Temple", 5), ("DakshinaChitra", 27.9), ("Kalakshetra Foundation", 19.3)],
        "history": [("Fort St. George", 2.9), ("Santhome Basilica", 6.5), ("Vivekanandar Illam", 1.9)],
    },
    "Jaipur": {
        "nature": [("Rambagh Palace Gardens", 4.3), ("Jal Mahal", 11), ("Kanak Vrindavan", 2.8)],
        "culture": [("Hawa Mahal", 4.7), ("City Palace", 0.5), ("Albert Hall Museum", 2.9)],
        "history": [("Amber Fort", 11), ("Nahargarh Fort", 9.5), ("Jaigarh Fort", 5.4)],
    },
    "Agra": {
        "nature": [("Mehtab Bagh", 26.0), ("Keetham Lake", 29), ("Taj Nature Walk", 31)],
        "culture": [("Agra Art Gallery",6 ), ("Subhash Emporium", 0.2), ("Shilpgram", 5.6)],
        "history": [("Taj Mahal", 5,9), ("Agra Fort", 3.1), ("Fatehpur Sikri", 37)],
    },
    "Gwalior": {
        "nature": [("Tighra Dam", 12), ("Gwalior Zoo", 18.5), ("hool Bagh", 5)],
        "culture": [("Jai Vilas Palace", 4.2), ("Kala Vithika", 3), ("Scindia Museum", 5)],
        "history": [("Gwalior Fort", 4), ("Tansen's Tomb", 1.0), ("Sun Temple", 100)],
    },
    "Varanasi": {
        "nature": [("Assi Ghat", 3), ("Tulsi Manas Mandir Garden", 1.1), ("Banaras Hindu University Campus", 1.2)],
        "culture": [("Kashi Vishwanath Temple", 3), ("Dashashwamedh Ghat",0.9 ), ("Bharat Kala Bhavan", 5.1)],
        "history": [("Sarnath", 10.0), ("Ramnagar Fort",14.7 ), ("Man Singh Observatory", 6.7)],
    },
    "Lucknow": {
        "nature": [("Gomti Riverfront", 3.9), ("Janeshwar Mishra Park", 3.4), ("Kukrail Forest", 11)],
        "culture": [("Bara Imambara",6.6 ), ("Rumi Darwaza", 0.2), ("Chowk Market", 0.8)],
        "history": [("Residency",5.5 ), ("Chhota Imambara", 2.7), ("Dilkusha Kothi", 8.6)],
    },
    "Amritsar": {
        "nature": [("Company Bagh", 0.5), ("Ram Tirath Ashram", ), ("Harike Wetland", 30)],
        "culture": [("Golden Temple", 2.5), ("Jallianwala Bagh", 2.0), ("Gobindgarh Fort", 3)],
        "history": [("Partition Museum", 2.1), ("Wagah Border", 31.2), ("Khalsa College", 27.0)],
    },
    "Hyderabad": {
        "nature": [("KBR National park", 2.4), ("Durgam Cheruvu", 4.0), ("Hussain Sagar Lake", 14.9)],
        "culture": [("Birla Mandir", 5.4), ("Charmina", 6.8), ("golconda", 11.5)],
        "history": [("Qutb Shahi Tombs", 10.5), ("Chowmahalla Palace", 12.2), ("Paigah Tombs", 12)],
    },
    "Pune": {
        "nature": [("Khadakwasla Dam", 18), ("Sinhagad Fort Gardens", 17), ("Pashan Lake", 33)],
        "culture": [("Shaniwar Wada", 3), ("Aga Khan Palace", 11), ("Pataleshwar Cave Temple",10)],
        "history": [("Sinhagad Fort", 32), ("Raja Dinkar Kelkar Museum", 29), ("Lal Mahal",1.3 )],
    },
    "Coimbatore": {
        "nature": [("Marudhamalai Temple",15.7 ), ("Aliyar Dam", 78), ("Black Thunder Water Park", 90)],
        "culture": [("Perur Pateeswarar Temple", 11), ("VOC Park", 8.9), ("Gedee Car Museum", 1.9)],
        "history": [("Gass Forest Museum", 4.3), ("Bhavani Sagar Dam", 60), ("Anamalai Tiger Reserve", 150)],
    },
    "Mysore": {
        "nature": [("Brindavan Gardens", 21), ("Karanji Lake", 23.4), ("Chamundi Hills", 9.4)],
        "culture": [("Mysore Palace", 3), ("St. Philomena's Church", 2.5), ("Rangacharlu Memorial Hall", 1.6)],
        "history": [("Jaganmohan Palace", 1.6), ("Lalitha Mahal", 5.7), ("Railway Museum", 7.2)],
    },
}



# Preferences for each place
preferences = {
    "Delhi": ["history", "culture", "nature"],
    "Jaipur": ["history", "culture", "nature"],
    "Agra": ["history", "culture", "nature"],
    "Gwalior": ["history", "culture", "nature"],
    "Amritsar": ["history", "culture", "nature"],
    "Mumbai": ["history", "culture", "nature"],
    "Hyderabad": ["history", "culture", "nature"],
    "Pune": ["history", "culture", "nature"],
    "Lucknow": ["history", "culture", "nature"],
    "Bhopal": ["history", "culture", "nature"],
    "Kolkata": ["history", "culture", "nature"],
    "Chennai": ["history", "culture", "nature"],
    "Coimbatore": ["history", "culture", "nature"],
    "Mysore": ["history", "culture", "nature"],
    "Varanasi": ["history", "culture", "nature"],
}


# Travel cost per mode
cost_per_km = {"car": 5, "train": 2, "flight": 10}
mode_thresholds = {"car": 100, "train": 500}  # km thresholds

def get_travel_mode_and_cost(distance):
    """Determine travel mode and cost based on distance."""
    if distance <= mode_thresholds["car"]:
        mode = "car"
        speed = 80  # Average speed in km/h
    elif distance <= mode_thresholds["train"]:
        mode = "train"
        speed = 100
    else:
        mode = "flight"
        speed = 500
    travel_time = round(distance / speed, 2)  # Time in hours
    cost = distance * cost_per_km[mode]
    return mode, cost, travel_time

def calculate_end_time(start_time, hours):
    """Calculate end time given start time and hours as a decimal."""
    start_hour, start_minute = map(int, start_time[:-3].split(":"))
    if "PM" in start_time and start_hour != 12:
        start_hour += 12
    if "AM" in start_time and start_hour == 12:
        start_hour = 0
    total_minutes = start_hour * 60 + start_minute + int(hours * 60)
    end_hour = (total_minutes // 60) % 24
    end_minute = total_minutes % 60
    am_pm = "AM" if end_hour < 12 else "PM"
    if end_hour == 0:
        end_hour = 12
    elif end_hour > 12:
        end_hour -= 12
    return f"{end_hour:02}:{end_minute:02} {am_pm}"

def generate_itinerary(start, interests, days, budget, num_people):
    """Generate a day-by-day travel itinerary within the given budget."""
    visited = {start}
    itinerary = []
    current_place = start
    total_cost = 0

    for day in range(1, days + 1):
        day_schedule = []
        if day > 1:
            distances_from_current = distances[places.index(current_place)]
            possible_destinations = [
                (places[i], distances_from_current[i])
                for i in range(len(places))
                if places[i] not in visited
            ]
            if not possible_destinations:
                break

            prioritized_destinations = sorted(
                possible_destinations,
                key=lambda x: (x[1], preferences[x[0]] == interests),
            )
            
            # Find the next affordable destination
            next_place = None
            for place, distance in prioritized_destinations:
                mode, cost, travel_time = get_travel_mode_and_cost(distance)
                if total_cost + cost <= budget:
                    next_place = place
                    break
            
            if next_place is None:
                break  # No affordable destination found

            mode, cost, travel_time = get_travel_mode_and_cost(distance)
            total_cost += cost
            visited.add(next_place)

            start_travel = "08:00 AM"
            end_travel = calculate_end_time(start_travel, travel_time)
            day_schedule.append({
                "time": f"{start_travel} - {end_travel}",
                "activity": f"Travel from {current_place} to {next_place} by {mode}"
            })

            current_place = next_place
        
        # Add attractions based on interests

        attractions_in_city = attractions.get(current_place, {})

        interest_attractions = attractions_in_city.get(interests, [])
        other_attractions = [attr for category, attrs in attractions_in_city.items() for attr in attrs if category != interests]
        
        # Prioritize attractions based on interests, but include others if needed
        day_attractions = interest_attractions + random.sample(other_attractions, max(0, 3 - len(interest_attractions)))
        day_attractions = day_attractions[:3]  # Limit to 3 attractions per day

        current_time = end_travel if day > 1 else "09:00 AM"
        for attraction, travel_distance in day_attractions:
            travel_to_attraction_time = travel_distance / 20
            visit_duration = 2  # Assuming a fixed visit duration of 2 hours for simplicity

            # Add travel to the attraction
            day_schedule.append({
                "time": f"{current_time} - {calculate_end_time(current_time, travel_to_attraction_time)}",
                "activity": f"Travel to {attraction} ({travel_distance} km)"
            })
            current_time = calculate_end_time(current_time, travel_to_attraction_time)

            # Add visit to the attraction
            day_schedule.append({
                "time": f"{current_time} - {calculate_end_time(current_time, visit_duration)}",
                "activity": f"Visit {attraction}"
            })
            current_time = calculate_end_time(current_time, visit_duration)

            # Update total cost for visiting the attraction
            attraction_cost = get_attraction_cost(attraction)
            total_cost += attraction_cost

        itinerary.append({"day": day, "place": current_place, "schedule": day_schedule})

    return itinerary, total_cost

def get_attraction_cost(attraction):
    """Calculate the cost for visiting a particular attraction."""
    # Define a basic cost model (this can be expanded to be more dynamic)
    attraction_costs = {
        "Historical Museum": 100,   # Example costs
        "Nature Park": 50,
        "Beach": 0,
        "Temple": 30,
        "Art Gallery": 80,
    }
    return attraction_costs.get(attraction, 50)  # Default cost if attraction not found
def generate_itinerary_gui():
    start_location = start_var.get()
    interests = vari.get()
    no_of_days = int(days_var.get())
    budget = float(budget_entry.get())
    num_people = int(people_combo.get())

    if start_location not in places:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Invalid starting location! Please choose from {places}.")
        return

    itinerary, total_cost = generate_itinerary(start_location, interests, no_of_days, budget, num_people)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "--- Travel Itinerary ---\n")
    for day_info in itinerary:
        result_text.insert(tk.END, f"Day {day_info['day']} in {day_info['place']}:\n")
        result_text.insert(tk.END, "  Schedule:\n")
        for activity in day_info["schedule"]:
            result_text.insert(tk.END, f"    {activity['time']}: {activity['activity']}\n")
        result_text.insert(tk.END, "\n")

    total_cost_per_person = total_cost * num_people
    result_text.insert(tk.END, f"Total Cost for {num_people} people: ₹{total_cost_per_person*num_people}\n")
    
    if total_cost*num_people > budget:
        result_text.insert(tk.END, f"Warning: The itinerary exceeds the budget by ₹{total_cost*num_people*num_people - budget}.")
    else:
        result_text.insert(tk.END, f"Remaining Budget: ₹{budget - total_cost*num_people*num_people}")
        
        if  budget - total_cost*num_people*num_people<0:
            
            result_text.insert(tk.END,f"WARNING:₹{budget - total_cost*num_people} is needed for your trip ")

        
    

# Add the rest of the code (Tkinter GUI setup) unchanged

# Create the main window
root = tk.Tk()
root.title("Travel Itinerary Generator")

heading_label = ttk.Label(root, text="WELCOME TO MINI TOURISM PLANNER", font=("Arial", 16, "bold"))
heading_label.grid(row=0, column=0, pady=10)

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Starting Location:").grid(column=0, row=0, sticky=tk.W)
start_var = tk.StringVar()
start_combo = ttk.Combobox(frame, textvariable=start_var, values=places)
start_combo.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Interests:").grid(column=0, row=1, sticky=tk.W)
vari = tk.StringVar()
interests_entry = ttk.Combobox(frame, textvariable=vari, values=opt)
interests_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Number of Days:").grid(column=0, row=2, sticky=tk.W)
days_var = tk.StringVar()
days_combo = ttk.Combobox(frame, textvariable=days_var, values=list(range(1, 6)))
days_combo.grid(column=1, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Budget (₹):").grid(column=0, row=3, sticky=tk.W)
budget_entry = ttk.Entry(frame)
budget_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Number of People:").grid(column=0, row=4, sticky=tk.W)
people_combo = ttk.Combobox(frame)
people_combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Example options
people_combo.grid(column=1, row=4, sticky=(tk.W, tk.E))

# Add a button to generate the itinerary
generate_button = ttk.Button(frame, text="Generate Itinerary", command=generate_itinerary_gui)
generate_button.grid(column=0, row=5, columnspan=2)

# Add a scrolled text widget for displaying results
result_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=20)
result_text.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))

# Configure grid padding
for child in frame.winfo_children():
    child.grid_configure(padx=6, pady=6)

# Start the Tkinter event loop
root.mainloop()
