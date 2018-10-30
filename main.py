def get_answer_on_presence(msg):
    response = {
        "response": 200,
    }

    if msg["action"] == "presence":

        response["year_of_birth"] = int(msg["year"])

    else:

        response["response"] = 400


    return response

