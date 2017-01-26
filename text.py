from twilio.rest import TwilioRestClient
#Twilio API

account_sid = "AC84e2cbe03e21554bb116961e88a34207" #Obtained from Twilio account 
auth_token = "2d6ff3615e535195732325d4f222f8ec"

client = TwilioRestClient(account_sid, auth_token) #create client object using the sid and token

client.messages.create(body = "Motion detected",  #body is the message, to is receiving number, from is twilio number
	to="2149015354",
	from_="+19725563796",
	)
	
