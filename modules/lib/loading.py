import time
import threading
import sys

class LoadingThread(threading.Thread):
    def __init__(self, message, loading_type='default'):
        super().__init__()
        self.message = message
        self.loading_type = loading_type
        self.progress = 0
        self.stop_flag = threading.Event()

    def stop(self):
        self.stop_flag.set()
    
    def is_run(self):
        return self.is_alive()

    
    def update_progress(self, progress):
        self.progress = progress

    def loading_default(self):
        animation = "|/-\\"
        idx = 0
        while not self.stop_flag.is_set():
            print(f"{self.message} {animation[idx % len(animation)]}", end="\r")
            idx += 1
            time.sleep(0.1)
        self.clear_line()

    def loading_horizontal(self):
        bar_length = 20
        while not self.stop_flag.is_set():
            filled_length = int(bar_length * self.progress)
            bar = '#' * filled_length + '-' * (bar_length - filled_length)
            print(f"{self.message} [{bar}] {self.progress * 100:.1f}%", end="\r")
            time.sleep(0.1)
        self.clear_line()

    def clear_line(self):
        sys.stdout.write("\033[K")
        sys.stdout.flush()

    def run(self):
        if self.loading_type == 'default':
            self.loading_default()
        elif self.loading_type == 'horizontal':
            self.loading_horizontal()


def main():
    message = "Loading..."

    loading_default = LoadingThread(message, 'default')
    loading_horizontal = LoadingThread(message, 'horizontal')

    loading_default.start()
    loading_horizontal.start()

    # Mengupdate kemajuan (progress) secara dinamis
    for i in range(101):
        loading_default.update_progress(i / 100)
        loading_horizontal.update_progress(i / 100)
        time.sleep(0.1)

    # Menghentikan loading
    loading_default.stop()
    loading_horizontal.stop()

    loading_default.join()
    loading_horizontal.join()


