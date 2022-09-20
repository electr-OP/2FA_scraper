import mailslurp_client
import time
import datetime
 


configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = "d71478d0bf10e52fac44ff2598a6e16600d7717d33c5c2b98e60f519fdce09c1"

all_cred = []

string = "31/03/2022"
  
element = datetime.datetime.strptime(string,"%d/%m/%Y")
  
tuple = element.timetuple()
timestamp = time.mktime(tuple)

def create_inbox_example():
    cred = []
    with mailslurp_client.ApiClient(configuration) as api_client:

        # create an inbox using the inbox controller
        api_instance = mailslurp_client.InboxControllerApi(api_client)
        inbox = api_instance.create_inbox(expires_at='31/03/2022 06:00')

        # check the id and email_address of the inbox
        assert len(inbox.id) > 0
        assert "mailslurp.com" in inbox.email_address
        cred.append(inbox.id)
        cred.append(inbox.email_address)
        return cred


def receive_email_and_extract_content_example(cred):
    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        # receive email for inbox 2
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = waitfor_controller.wait_for_latest_email(inbox_id=cred[0], timeout=30000, unread_only=True)

        # assert email.subject == "Hello inbox 2"

        # extract content from body
        body = email.body
        print('---------------', body , '-----------------------')
        code = (str(body)[str(body).index('<strong>')+8:str(body).index('</strong>')])
        return code

def test_can_list_inboxes(i):
    # use the with keyword to create an api client
    with mailslurp_client.ApiClient(configuration) as api_client:
        # create an inbox using the inbox controller
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inboxes = inbox_controller.get_all_inboxes(page = i)

        # pagination properties
        assert inboxes.total_pages > 0
        assert inboxes.total_elements > 0
        # view contents
        # assert len(inboxes.content[0].id) > 0
        return inboxes


for i in range(52):
    create_inbox_example()

# for i in range(1,4):
#     recs = test_can_list_inboxes(i)
#     with open(r'statics\text\email_list.txt', 'a') as f:
#         for rec in recs.content:
#             f.write(rec.id + ', ' + rec.email_address+'\n')


        # cred.append(rec.id)
        # cred.append(rec.email_address)
        # all_cred.append(cred)

    # for item in 
    # f.writeline(str(all_cred))