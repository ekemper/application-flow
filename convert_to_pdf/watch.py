import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from convert import html_to_pdf  # Assuming convert.py has the html_to_pdf function

# Define the file to watch
HTML_FILE = Path(__file__).parent / "temp.html"

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == str(HTML_FILE):
            print(f"{HTML_FILE} has been modified. Rendering PDF...")
            html_to_pdf(str(HTML_FILE), "output.pdf")
            print("PDF successfully rendered as output.pdf")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(HTML_FILE.parent), recursive=False)

    print(f"Watching {HTML_FILE} for changes...")
    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()