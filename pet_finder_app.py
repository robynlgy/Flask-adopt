import requests

BASE_URL = 'https://api.petfinder.com/ '

# would be from first function that we didnt make
API_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJhc1NDaWdqWnc2TTFMSU9WZEg2RWRtUkFJQWZ1VFZmSVFxN1M2dURuRzlXN1drU0VweSIsImp0aSI6IjdkZDk0MzQ4MmYzMjdkNzExNDU0N2ZjOWQ0NmQyMGE0ZmUyZjY4MTZiYzY1ZTNkNjNiMzljNWUyNzZjYjAyNDNlOTViNjkxNGViM2EzMmU0IiwiaWF0IjoxNjQ4ODYyMjY1LCJuYmYiOjE2NDg4NjIyNjUsImV4cCI6MTY0ODg2NTg2NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.bNw5ubJOE9klxyLWFTGsmE3jPlopbzYlV90ZYQYj8MQQqYtmRcBt6JkJfWVhrjqLm7sHWzp4oD7yTEQ2sLJ-DU5NxmvA0WNkf_Q3co9MZNaPtmHi04ALLZKb-c1dvoysHTJxaqWB7cFQL0HngfM7KjgWTFtkS85vES-BU037cUJ5tc0UXcW3WhEZ9lOfCIEm1tsx1GTQAstVYzns66aeZj3y0JOCSubEhJlsT9ECSakIO0VIbLTs_7AhHFkJRaOOaj4zPQycfvZrtixOJtVbq32GV1N9agtXWz0uHEVOImHeVKYGhHUr6ELrOgq5PNQjVPZzWEWkPLlmz92Ns77c4A'



def get_random_pet():
    """Get random pet from /animals url"""

    resp = requests.get(
        "https://api.petfinder.com/v2/animals",
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJhc1NDaWdqWnc2TTFMSU9WZEg2RWRtUkFJQWZ1VFZmSVFxN1M2dURuRzlXN1drU0VweSIsImp0aSI6IjdkZDk0MzQ4MmYzMjdkNzExNDU0N2ZjOWQ0NmQyMGE0ZmUyZjY4MTZiYzY1ZTNkNjNiMzljNWUyNzZjYjAyNDNlOTViNjkxNGViM2EzMmU0IiwiaWF0IjoxNjQ4ODYyMjY1LCJuYmYiOjE2NDg4NjIyNjUsImV4cCI6MTY0ODg2NTg2NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.bNw5ubJOE9klxyLWFTGsmE3jPlopbzYlV90ZYQYj8MQQqYtmRcBt6JkJfWVhrjqLm7sHWzp4oD7yTEQ2sLJ-DU5NxmvA0WNkf_Q3co9MZNaPtmHi04ALLZKb-c1dvoysHTJxaqWB7cFQL0HngfM7KjgWTFtkS85vES-BU037cUJ5tc0UXcW3WhEZ9lOfCIEm1tsx1GTQAstVYzns66aeZj3y0JOCSubEhJlsT9ECSakIO0VIbLTs_7AhHFkJRaOOaj4zPQycfvZrtixOJtVbq32GV1N9agtXWz0uHEVOImHeVKYGhHUr6ELrOgq5PNQjVPZzWEWkPLlmz92Ns77c4A"},
        params = {"limit":5}
    )
    # breakpoint()
    return resp.json()

