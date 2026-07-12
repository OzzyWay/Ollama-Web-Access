from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
from functools import lru_cache
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


EXCLUDE = {
    "style",
    "script",
    "head",
    "title",
    "meta",
    "[document]",
    "noscript",
}


class HTMLExtractor:

    def __init__(self, exclude_tags=None, timeout=10, cache_size=128):
        self.exclude_tags = exclude_tags or EXCLUDE
        self.timeout = timeout

        self._extract_cached = lru_cache(
            maxsize=cache_size
        )(self._extract_impl)


    def is_visible(self, element):

        if isinstance(element, Comment):
            return False

        parent = element.parent.name if element.parent else None

        return parent not in self.exclude_tags



    def extract_text(self, body):

        if isinstance(body, bytes):
            body = body.decode(
                "utf-8",
                errors="ignore"
            )


        soup = BeautifulSoup(
            body,
            "html.parser"
        )


        texts = []


        for element in soup.find_all(text=True):

            if self.is_visible(element):

                text = element.strip()

                if text:
                    texts.append(text)



        return "\n".join(texts)



    def _extract_impl(self, url):
        return self._fetch_and_extract(url)



    def _fetch_and_extract(self, url):

        try:

            headers = {
                "User-Agent":
                (
                    "Mozilla/5.0 "
                    "(X11; Linux x86_64) "
                    "Chrome/120 Safari/537.36"
                )
            }


            response = requests.get(
                url,
                headers=headers,
                timeout=self.timeout
            )


            response.raise_for_status()


            text = self.extract_text(
                response.content
            )


            if not text:

                logger.warning(
                    f"No text found: {url}"
                )

                return ""


            return text



        except requests.RequestException as e:

            logger.error(
                f"Request failed {url}: {e}"
            )

            return ""



        except Exception as e:

            logger.error(
                f"Extraction error {url}: {e}"
            )

            return ""



    def from_url(self, url, use_cache=True):

        if isinstance(url, dict):
            url = url.get("url")


        if not isinstance(url, str):

            raise TypeError(
                f"URL must be string, got {type(url)}"
            )


        if not url.startswith(
            ("http://", "https://")
        ):

            url = "https://" + url



        if use_cache:
            return self._extract_cached(url)


        return self._fetch_and_extract(url)



_default_extractor = HTMLExtractor()



def extract_from_url(url):

    return _default_extractor.from_url(url)



def extract_from_html(html):

    return _default_extractor.extract_text(html)