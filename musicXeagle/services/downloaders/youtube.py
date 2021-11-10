# Calls Music 1 - Telegram bot for streaming audio in group calls

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from os import path

from yt_dlp import YoutubeDL

from musicXeagle.config import DURATION_LIMIT
from musicXeagle.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, "
            f"the provided video is {duration} minute(s)",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, "
            f"the provided video is {duration} minute(s)",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
