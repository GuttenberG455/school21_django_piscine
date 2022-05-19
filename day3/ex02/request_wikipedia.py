
import sys
import requests
import json
import dewiki


def request_to_wiki(searched_str):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "parse",
        "page": searched_str,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }
    try:
        request = requests.get(url=url, params=params)
        request.raise_for_status()
    except requests.HTTPError as e:
        return print(e)
    try:
        data = json.loads(request.text)
    except json.decoder.JSONDecodeError as e:
        return print(e)
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    return dewiki.from_string(data["parse"]["wikitext"]["*"])


def get_info_from_wiki(searched_str):
    try:
        f = open(f"{searched_str}.wiki".replace(' ', '_'), "w")
        f.write(request_to_wiki(searched_str))
        f.close()
    except Exception as e:
        return print(e)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_info_from_wiki(sys.argv[1])
    else:
        print("Wrong Input! Type exactly one argument")
