import tkinter as tk
import webbrowser

# Create the main window
window = tk.Tk()
window.title("TIEF Browser")

# Create the URL bar
url_frame = tk.Frame(window)
url_bar = tk.Entry(url_frame)
url_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Create the back and forward buttons
back_button = tk.Button(url_frame, text="<")
forward_button = tk.Button(url_frame, text=">")
back_button.pack(side=tk.LEFT)
forward_button.pack(side=tk.LEFT)

# Create the refresh button
refresh_button = tk.Button(url_frame, text="Refresh")
refresh_button.pack(side=tk.RIGHT)

# Create the webview
webview = tk.Text(window)

# Pack the widgets
url_frame.pack(side=tk.TOP, fill=tk.X)
webview.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Set the custom styles
# style = """
#     * {
#         font-family: sans-serif;
#          color: white;
#         background-color: #00008B;
#     }
#     #url_frame {
#         background-color: #00008B;
#     }
#     #url_bar {
#         background-color: #00008B;
#         border: none;
#         color: white;
#     }
#     #back_button, #forward_button, #refresh_button {
#         background-color: #00008B;
#         color: white;
#         border: none;
#     }
# """
# webview.tag_configure("style", font=("sans-serif", 12))
# webview.insert("1.0", style, "style")

# Bind the buttons to their respective functions
def go_back():
    webbrowser.back()

def go_forward():
    webbrowser.forward()

def refresh():
    webbrowser.refresh()

back_button.config(command=go_back)
forward_button.config(command=go_forward)
refresh_button.config(command=refresh)

# Start the main loop
window.mainloop()