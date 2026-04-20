from winotify  import Notification, audio
import gui

def notify() -> None:
    toast = Notification(
        app_id="wmbar",
        title="WMBar is running",
        msg="WMBar is running, press Ctrl+Space to start working",

    )
    toast.set_audio(audio.Mail, loop=False)
    toast.show()

def check_for_updates() -> None:
    """
    Тут будет проверка на обновления
    Возможно я выведу это в отдельный файл updater.py
    """

if __name__ == "__main__":
    notify()
    gui.start()