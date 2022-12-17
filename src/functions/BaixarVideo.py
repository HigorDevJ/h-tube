import io
import re
import pytube
from io import BytesIO
from colorama import Fore, Style
import telebot

# Responsabilidade Unica


class BaixarVideo:
    def __init__(self, bot_token):
        self.bot_token: str = bot_token
        self.yt = pytube.YouTube(self.youtube_url).streams.first()
        self.bot = telebot.TeleBot(self.bot_token)
        self.buffer = BytesIO()

    def isValidUrl(youtube_url, username):
        regex = ("((http|https)://)(www.youtube)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        link = re.compile(regex)

        if re.search(link, youtube_url):  # type: ignore
            print(
                f"User: {username} | [{Fore.GREEN}!{Style.RESET_ALL}] Url Valida!")
            return True
        else:
            print(
                f"User: {username} | [{Fore.RED}!{Style.RESET_ALL}] Url Invalida!")
            return False

    def videoInformation(video):
        InfosVideo = []

        InfosVideo.append(video.title)
        InfosVideo.append(f"{video.length//60}min e {video.length%60}s")
        InfosVideo.append(
            f"{video.publish_date.day}/{video.publish_date.month}/{video.publish_date.year}")
        InfosVideo.append(video.thumbnail_url)
        InfosVideo.append(str(video.views))

        return InfosVideo

    def download(streams, qualidade):
        stream = streams.get_by_itag(int(qualidade))
        path = stream.download()
