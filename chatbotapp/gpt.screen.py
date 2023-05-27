import os
import openai
import customtkinter as ctk
#18:19
def generate():
    prompt = "Please generate 10 ideas for coding projects. "
    lenguage = lenguage_dropdown.get()
    prompt += "The programin leguange is " + lenguage + ". "
    difficuty = difficuty_value.get()
    prompt += "The Difficuty is " + difficuty + ". "

    if checkbox1.get():
        prompt += "The project should include a database"
    if checkbox2.get():
        prompt += "The project should include a API."

    print(prompt)
# here i put chagpt code
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

root = ctk.CTk()
root.geometry("750x750")
root.title("ChatGpt Game Idea Generator")
#color theme
ctk.set_appearance_mode("Dark")
#add labels an size fonts
title_label = ctk.CTkLabel(root, text="project gerenate ideas", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx="10", pady=(40, 20))
#crete interface
frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)
#cretate an interface into the interface
lenguage_frame = ctk.CTkFrame(frame)
lenguage_frame.pack(padx=100, pady=(20, 5), fill="both")
lenguage_frame = ctk.CTkLabel(
lenguage_frame, text="An Task", font=ctk.CTkFont(weight="bold"))
lenguage_frame.pack()
lenguage_dropdown = ctk.CTkComboBox(lenguage_frame, values=["java", "python", "c++", "JavaScript", "MongoDB"])
lenguage_dropdown.grid(pady=10, padx=10)
#box options button
difficuty_frame = ctk.CTkFrame(frame)
difficuty_frame.pack(padx=100, pady=5, fill="both")
difficuty_label = ctk.CTkLabel(difficuty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficuty_label.pack()
#option botton
difficuty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(difficuty_frame, text="Easy", variable=difficuty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(difficuty_frame, text="Medium", variable=difficuty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(difficuty_frame, text="Hard", variable=difficuty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)
#box of the features
features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
#check boxs
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)
#button and put that gerenre function
button = ctk.CTkButton(frame, text="Generate Ideas", command=generate)
button.pack(padx=100, fill="x", pady=(5, 20))
#text box for chatGPT
result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

root.mainloop()


