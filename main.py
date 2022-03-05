import pathlib
import sanic
import typing
import json
from sanic import response

app = sanic.Sanic(__name__)


def load_content(initial_directory: typing.Union[str, pathlib.Path]) -> dict:
    # Each directory in initial_directory contains a data.json file with the content of the directory.
    # The "files" key contains the list of files in the directory.
    # The "directories" key contains the list of subdirectories in the directory.

    # This function will run recursively through the directories and return a dictionary with the content of the
    # provided directory. The dictionary will have the following structure:

    example_content = {
        "images": {
            "__TYPE__": "DIRECTORY",
            "weather": {
                "__TYPE__": "DIRECTORY",
                "icons": {
                    "__TYPE__": "DIRECTORY",
                    "partly_cloudy": {
                        "__TYPE__": "IMAGE"
                    },
                    "sunny": {
                        "__TYPE__": "IMAGE"
                    }
                }
            }
        }
    }

    # The __TYPE__ key is used to determine the type of the content.
    # The value of the __TYPE__ key can be "DIRECTORY" or "IMAGE".
    # If the value of the __TYPE__ key is "DIRECTORY", the content of the directory is a dictionary with the
    # content of the subdirectories.
    # If the value of the __TYPE__ key is "IMAGE", the content of the directory is a dictionary with the content
    # of the image.






@app.route('/')
async def root(request):
    return response.redirect("https://soosbot.com/faq#content-delivery-network")
