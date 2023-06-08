import re
import os
import openai
from typing import *
openai.organization = "org-hRvtVqg73V5RwDiq5NbCp6ce"
openai.api_key = "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"
openai.Model.list()

initial_prompt = """
Hello ChatGPT, I am a friendly bus station.
My user said: "{input}"
I need you to give me one or more of the following instructions.
Remember to put a newline between each instruction.
Say nothing else.
Permitted instructions:
{permitted_instructions}
"""

second_prompt = """
Here are the results of your instructions:
{command_and_result_string}
Remember, the user said: "{input}". Answer his question.
"""


def ask_gpt(prompt, tokens=200):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=tokens,
        temperature=0
    )
    return response.choices[0].text


command_definitions = dict()
# define a wrapper to auto fill command_definitions:
def wrap_command(fptr: Callable) -> Callable:
    fname = fptr.__name__.upper()
    command_definitions[fname] = {
        "parameters": list(fptr.__annotations__.keys())[:-1], # last key is "return"
        "description": fptr.__doc__,
        "fptr": fptr,
    }
    command_definitions[fname]["GPT_FORMAT"] = ";".join(
        [fname] + ["REPLACE_WITH_" + param.upper() for param in command_definitions[fname]["parameters"]])
    return fptr


@wrap_command
def unclear_input() -> str:
    """Return an unclear input message"""
    return "UNCLEAR_INPUT"


@wrap_command
def get_time() -> str:
    """Return time"""
    # FIXME - replace this with an API call to an NTP server
    return "The time is 12:00 PM."


@wrap_command
def get_json_full_transit_directions(station_1: str, station_2: str) -> str:
    """Takes two station names and returns a JSON string from Google Maps, with full directions"""
    # use json.dumps(j)
    return


@wrap_command
def get_bus_schedule_for_station(station_name: str) -> str:
    # FIXME - replace this with an API call to Israeli Ministry of Transportation
    s = ""
    s += f"The bus schedule for station {station_name} is as follows:"
    s += f"271: 10:00, 11:00, 12:00, 13:00, 14:00, 15:00"
    s += f"272: 10:00, 11:00, 12:00, 13:00, 14:00, 15:00"
    s += f"273: 10:00, 11:00, 12:00, 13:00, 14:00, 19:00"
    return s

@wrap_command
def get_bus_source_and_destinations(bus_number: str) -> str:
    # FIXME - replace this with an API call to Israeli Ministry of Transportation
    s = ""
    s += "Bus 271 goes from Station A to Station B.\n"
    s += "Bus 272 goes from Station B to Station C.\n"
    s += "Bus 273 goes from Station C to Station D.\n"
    return s


@wrap_command
def get_raw_bus_navigation_instructions(station_1: str, station_2: str) -> str:
    # FIXME - replace this with an API call to Google Maps
    s = ""
    s += f"Walk 100 meters to station {station_1}."
    s += f"Take bus 271 to station {station_2}."
    s += f"Walk 200 meters to your destination."
    return s


def get_full_response_for_input(input: str) -> str:
    prompt = initial_prompt.strip().format(
        input=input,
        permitted_instructions="\n".join([v["GPT_FORMAT"] for v in command_definitions.values()])
    )
    response = ask_gpt(prompt)
    requested_commands_and_args = [command.split(";") for command in response.split("\n") if command]
    requested_commands = [command[0] for command in requested_commands_and_args]
    requested_args = [command[1:] for command in requested_commands_and_args]
    requested_commands_and_args = {
        command: args
        for command, args in zip(requested_commands, requested_args)
    }
    command_and_result = {
        ";".join([command]+args): command_definitions[command]["fptr"](*args)
        for command, args in requested_commands_and_args.items()
    }
    command_and_result_string = "\n".join(
        [f"{command} -> \"{result}\"" for command, result in command_and_result.items()])
    prompt = second_prompt.strip().format(
        input=input,
        command_and_result_string=command_and_result_string
    )
    response = ask_gpt(prompt, tokens=400) 
    return response


response = get_full_response_for_input("I want to go from station B to station D.")
print(response)




































