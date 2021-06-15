from mycroft import MycroftSkill, intent_file_handler


class RosInterface(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interface.ros.intent')
    def handle_interface_ros(self, message):
        self.speak_dialog('interface.ros')


def create_skill():
    return RosInterface()

