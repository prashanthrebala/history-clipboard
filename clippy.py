from clipboard_manager import ClipboardManager
import os

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), 'data', 'data.json')
    clipboard_manager = ClipboardManager(file_path)

    try:
        clipboard_manager.load_history_from_file()
        clipboard_manager.start_listener()
    finally:
        print("History clipboard closed")
