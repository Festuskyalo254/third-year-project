
import tkinter as tk
from tkinter import ttk

import mysql
import requests
from mysql.connector import cursor

# Window initialization and settings
window = tk.Tk()
window.title("Car Engine Diagnostic System Dashboard")
window.geometry('1000x800')
window.resizable(width=False, height=False)

# Title
label = tk.Label(window, text=" Dashboard ", font=("Impact", 35, "bold"), fg="#6162FF", bg="white")
label.grid(row=0, column=1, columnspan=2, pady=10, padx=10)

# Label for the combobox
label = tk.Label(window, text="Select a symptom:", font=("Goudy old style", 15,), bg="#E7E6E6")
label.grid(row=1, column=1, columnspan=2, pady=10, padx=10)

#database connection
connection = mysql.connector.connect( host='localhost',
                                      user = 'root',
                                      port = '3306',
                                      password = '1234#',
                                      database = 'carenginesystem')
c = connection.cursor()




#symptom lists
symptom_list = {
    "Engine Not Starting":{
        "conditions": "Engine Not Starting",
        "problem": "Dead Battery",
        "recommendation": "Jumpstart the Car or replace the battery if necessary."
    },

    "Excessive Smoke from Exhaust":{
        "conditions": "Excessive Smoke from Exhaust",
        "problem": "There can be several causes for excessive smoke, such as worn piston rings, faulty valve seals, or burning oil. The color of the smoke can help narrow down the problem:",
        "recommendation": "* **Blue smoke:** This indicates burning oil. It could be caused by worn piston rings, valve seals, or a turbocharger issue.  \n* **Black smoke:** This suggests a rich fuel mixture, which could be due to a faulty fuel injector, clogged air filter, or malfunctioning mass airflow sensor.  \n* **White smoke:** This might be caused by coolant burning in the engine, which could be a sign of a blown head gasket or cracked engine block.  \n**It's recommended to consult a mechanic for a proper diagnosis and repair.**"
    },
    "Engine Misfire":{
        "conditions": "Engine Misfire",
        "problem": "Engine misfire can occur due to faulty spark plugs, ignition coil problems, or issues with the fuel system. ",
        "recommendation": "Check spark plugs for wear or fouling, and consider replacing them if necessary. Inspect the ignition coils for damage. If the problem persists, consult a mechanic for further diagnosis."
    },
    "Engine Leakage":{
        "conditions": "Engine Leakage",
        "problem": "Leakage of fluids from the engine can indicate worn seals, gaskets, or loose connections. Identifying the leaking fluid is crucial for diagnosis.",
        "recommendation": "Locate the source of the leak and determine the type of fluid. Tighten loose connections if possible. For major leaks, consult a mechanic for repair."
    },
    "Engine Jerking or Hesitating":{
        "conditions": "Engine Jerking or Hesitating",
        "problem": "This could be caused by a variety of factors, such as a dirty fuel filter, faulty spark plugs, or problems with the fuel injection system.",
        "recommendation": "Try replacing the fuel filter. Check and replace spark plugs if needed. If the issue persists, consult a mechanic for a more thorough diagnosis."
    },
    "Poor Engine Performance":{
        "conditions": "Poor Engine Performance",
        "problem": "Several factors can contribute to poor engine performance, including clogged air filters, dirty fuel injectors, or worn spark plugs.",
        "recommendation": "Replace the air filter regularly. Clean or replace fuel injectors if necessary. Check and replace spark plugs. If the problem persists, consult a mechanic for further diagnosis."
    },
    "Oil Leak":{
        "conditions": "Oil Leak",
        "problem": "An oil leak can indicate worn seals, gaskets, or loose connections. It's important to address oil leaks promptly to prevent engine damage.",
        "recommendation": "Locate the source of the leak and determine the severity. Tighten loose connections if possible. For major leaks, consult a mechanic for repair."
    },
    "Battery Drain": {
        "conditions": "Battery Drain",
        "problem": "A battery drain can be caused by a faulty alternator, leaving lights on, or parasitic drain from electronic devices.",
        "recommendation": "Check if the alternator is properly charging the battery. Ensure all lights are turned off when the car is not in use. If the drain persists, consult a mechanic to identify and fix the parasitic drain."
    },
   "Rough Idle": {
        "conditions": "Rough Idle",
        "problem": "Rough idle can be caused by a variety of factors, such as dirty throttle body, faulty spark plugs, or vacuum leaks.",
        "recommendation": "Clean the throttle body according to your car's manual. Check and replace spark plugs if necessary. Inspect for vacuum leaks and tighten loose connections. If the problem persists, consult a mechanic for further diagnosis."
    },
   "Check Engine Light on": {
        "conditions": "Check Engine Light on",
        "problem": "The Check Engine Light indicates a problem detected by the engine computer. The specific problem can vary depending on the fault code stored. ",
        "recommendation": "Use an OBD-II"

},
  "Engine Stalling": {
        "conditions": "Engine Stalling",
        "problem": "Stalling can occur due to a variety of reasons, including fuel system issues, ignition problems, or sensor malfunctions.",
        "recommendation": "Fuel System Issues:A lack of fuel reaching the engine can cause stalling. This could be due to a clogged fuel filter, faulty fuel pump, or malfunctioning fuel injectors.  \nIgnition Problems: Faulty spark plugs, worn ignition coils, or problems with the ignition module can prevent proper spark generation, leading to stalling.  \nSensor Malfunctions: Faulty sensors like the crankshaft position sensor or mass airflow sensor can send incorrect data to the engine computer, causing stalling.  \nIt's recommended to consult a mechanic for a proper diagnosis and repair. In the meantime, here are some additional tips:"
            "Ensure you have sufficient fuel in the tank"
            "If the car stalls while driving, attempt to safely pull over to the side of the road and turn off the engine. Try restarting the engine after a few minutes"
            "If the problem persists, avoid driving the car and seek professional help from a mechanic"

    },
}

condition_list = [symptom["conditions"] for symptom in symptom_list.values()]



# Combobox for a selection of a symptom
symptom_combobox = ttk.Combobox(window, values=condition_list, width=40, height=1)
symptom_combobox.grid(row=2, column=1, columnspan=2, pady=10, padx=10)

# Function for search
def Diagnose_now():
    selected_item = symptom_combobox.get()
    if selected_item in symptom_list:
        text_area.delete("1.0", tk.END)  # Clear the output text area
        # Access information using the selected_item key
        selected_symptom = symptom_list[selected_item]
        text_area.insert(tk.END, f"\n**Diagnosis:**\n")

        # Insert all information from the selected symptom dictionary
        text_area.insert(tk.END, f"Conditions: {selected_symptom['conditions']}\n")
        text_area.insert(tk.END, f"Problem: {selected_symptom['problem']}\n")
        text_area.insert(tk.END, f"Recommendation: {selected_symptom['recommendation']}\n")

    else:
            text_area.insert(tk.INSERT, "Selected symptom not found in the list\n"
                                        "find solution  from the online source.")

# Button search for a defined symptom
Diagnose_button = tk.Button(window, text="Diagnose", command=Diagnose_now, font=("Goudy old style", 15,), bg="#6162FF",
                          height=1, width=10)
Diagnose_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10)

# Label or
label_or = tk.Label(window, text="OR:", font=("Goudy old style", 15,), bg="#E7E6E6")
label_or.grid(row=4, column=1, columnspan=2)

# Functions for the entry box
def symptom_enter(e):
    symptom_entry.delete(0, 'end')

def symptom_leave(e):
    if symptom_entry.get() == '':
        symptom_entry.insert(0, 'Enter Symptom')

# Entry box for the symptom option
symptom_entry = tk.Entry(window, font=("Goudy old style", 15,), bg="#E7E6E6", width=30)
symptom_entry.insert(0, " Enter Symptom")
symptom_entry.bind("<FocusIn>", symptom_enter)
symptom_entry.bind("<FocusOut>", symptom_leave)
symptom_entry.grid(row=5, column=1, columnspan=2, pady=10, padx=10)

# Text area for the display of the results
text_area = tk.Text(window, width=130, height=10, font=("Aptos Display", 10,), bg="#E7E6E6")
text_area.grid(row=7, column=1, columnspan=2, pady=10, padx=30)


# retrieve from database
def get_solution_from_database():
    # Retrieve user entered symptom
    user_entered_symptom = symptom_entry.get().strip()
    text_area.delete("1.0", tk.END)

# Build select specific columns
    query = f"SELECT symptom, problem, recommendation FROM diagnose WHERE symptom = '{user_entered_symptom}'"
    c.execute(query)
# Fetch results and display in text area
    result = c.fetchone()
    if result:
 # Access each column separately for better formatting
        symptom, problem, recommendation = result
        text_area.insert(tk.INSERT,f"**Diagnosis Result**\n\n")
        text_area.insert(tk.INSERT,
            f"Symptom:** {symptom}\nProblem:** {problem}\nRecommendation:** {recommendation}")
    else:
        text_area.insert(tk.INSERT, f"Symptom '{user_entered_symptom}' not found in the database.")


# Get solution button
solution_button = tk.Button(window, text="Get Solution from database", command=get_solution_from_database,
                             font=("Goudy old style", 15,), bg="#6162FF")
solution_button.grid(row=6, column=1, columnspan=2, pady=10, padx=10)

#method back
def back():
    window.destroy()
    import Login

#back button
back_button = tk.Button(cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
back_button.grid(row=8,column=1,columnspan=2,pady=10,padx=10)

window.mainloop()
