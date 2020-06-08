from twilio.twiml.messaging_response import MessagingResponse
from app.model import DonorModel


def reply(message):
    resp = MessagingResponse()
    try:
        blood_group = message.split(" ")[0]
        city = message.split(" ")[1].lower()
    except IndexError:
        resp.message("Please enter both Blood Group and City in the following format:\n*B+ Islamabad*")
        return str(resp)
    donors = DonorModel.query.filter_by(blood_group=blood_group).filter_by(city=city).all()
    if len(donors) == 0:
        resp.message("There is no donor currently. Please check after some while.")
        return str(resp)
    message = " "
    for donor in donors:
        city = donor.city.title()
        message = message + f"\n*{donor.name}*\n{donor.blood_group}   {city}\n{donor.contact_no}"
    resp.message(f"{message}")
    return str(resp)
