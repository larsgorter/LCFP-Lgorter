# Create a new class, SMS_store. The class will
# instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
# (has_been_viewed, from_number, time_arrived, text_of_SMS)
# my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# Makes new SMS tuple, inserts it after other messages
# in the store. When creating this message, its
# has_been_viewed status is set False.
# my_inbox.message_count()
# Returns the number of sms messages in my_inbox
# my_inbox.get_unread_indexes()
# Returns list of indexes of all not-yet-viewed SMS messages
# my_inbox.get_message(i)
# Return (from_number, time_arrived, text_of_sms) for message[i] # Also change its state to "has been viewed".
# If there is no message at position i, return None
# my_inbox.delete(i)
# Delete the message at index i my_inbox.clear()
# Delete all messages from inbox


class SMSStore:

    def __init__(self):
        self.message = []
        self.view_state = []

    def add_new_arrival(self, origin, arrivalt, messagecontent):
        self.message.append((origin, arrivalt, messagecontent))
        self.view_state.append(False)

    def message_count(self):
        return len(self.message)

    def get_unread_indexes(self):
        indices = []
        for (i, v) in enumerate(self.view_state):
            if not v:
                indices.append(i)
        return indices

    def get_message(self, i):
        try:
            self.view_state[i] = True
            return self.message[i]
        except:
            return None

    def delete(self, i):
        self.message.remove(self.message[i])
        self.view_state.remove(self.view_state[i])

    def clear(self):
        self.message = []
        self.view_state = []

Inbox = SMSStore()

Inbox.add_new_arrival("0123456789", "2020-1-2 12:22:22", "hello world")
Inbox.add_new_arrival("0022334481", "2020-1-2 12:22:32", "Bye World")
Inbox.add_new_arrival("009988776655", "2020-1-2 12:22:22", "What World")

print(Inbox.get_unread_indexes())
print(Inbox.get_message(1))
print(Inbox.message_count())