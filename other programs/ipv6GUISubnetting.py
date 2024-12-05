import tkinter as tk
from ipaddress import IPv6Network


def calculate_subnets():
    try:
        network = IPv6Network(entry_network.get())
        prefix_length = int(entry_prefix.get())
        subnets = list(network.subnets(new_prefix=prefix_length))

        result_text = "\n".join(str(subnet) for subnet in subnets)
        text_result.config(state=tk.NORMAL)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result_text)
        text_result.config(state=tk.DISABLED)
    except Exception as e:
        text_result.config(state=tk.NORMAL)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"Error: {str(e)}")
        text_result.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("IPv6 Subnet Calculator")

# Create and place the widgets
label_network = tk.Label(root, text="IPv6 Network (e.g., 2001:db8::/32):")
label_network.grid(row=0, column=0, padx=10, pady=5)

entry_network = tk.Entry(root, width=40)
entry_network.grid(row=0, column=1, padx=10, pady=5)

label_prefix = tk.Label(root, text="New Prefix Length (e.g., 48):")
label_prefix.grid(row=1, column=0, padx=10, pady=5)

entry_prefix = tk.Entry(root, width=40)
entry_prefix.grid(row=1, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate Subnets", command=calculate_subnets)
button_calculate.grid(row=2, columnspan=2, pady=10)

text_result = tk.Text(root, height=10, width=60, state=tk.DISABLED)
text_result.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()