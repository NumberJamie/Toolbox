import string


class UrlString:
    """
    Utility class for handling URL-related string checks.
    """

    def __init__(self):
        self._chars = string.ascii_letters + string.digits
        self._url_safe = self._chars + '$-_.+!*\'(),'
        self._url_reserved = ';/?:@=&'
        self._url_unsafe = """\" <>#%{}|\^~[]`"""

    def is_url_save(self, str_input: str) -> bool:
        """
        Checks whether the provided string is safe to include into a URL.

        :param str_input: The input string to be checked.
        :return: True if the string is URL-safe, otherwise False.
        """
        return all(char in self._url_safe for char in str_input)

    def is_url_reserved(self, str_input: str) -> bool:
        """
        Checks whether any character in the provided string has a reserved URL character.

        :param str_input: The input string to be checked.
        :return: True if any reserved URL character is present, otherwise False.
        """
        return any(char in self._url_reserved for char in str_input)

    def is_url_unsafe(self, str_input: str) -> bool:
        """
        Checks whether any character in the provided string has a URL unsafe character.

        :param str_input: The input string to be checked.
        :return: True if any unsafe URL character is present, otherwise False.
        """
        return any(char in self._url_unsafe for char in str_input)


url_string = UrlString()
