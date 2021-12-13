class coderDecoder:
    def __init__(self, message=None, key=None, print_info=True):
        self.abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '.', ',', '[', ']', '{', '}', ':', ';', "'", '"']
        if print_info:
            if message == None:
                message = input('What is your message?\n')
            if key == None:
                while True:
                    key = int(input('what is the key? (from 1 to {})\n'.format(len(self.abcs))))
                    if key >= 1 and key < len(self.abcs):
                        break
                    else:
                        print('inccorrect number')
            if code_decode == None:
                code_decode = input('Would you like to code or decode (code/decode)\n')
        
        self.message = message
        self.key = key
        self.finished = ''
        self.print_info = print_info

    def code(self):
        message = list(self.message)
        new_message = []
        new_message_str = ''
        
        for i in range(len(message)):
            for l in range(len(self.abcs)):
                if self.abcs[l] == message[i]:
                    try:
                        new_message.append(self.abcs[l + self.key])
                    except:
                        if (l + self.key) >= len(self.abcs):
                            loc = (l + self.key) - len(self.abcs)
                            new_message.append(self.abcs[loc])
        for item in new_message:
            new_message_str += item
        
        if self.print_info:
            print('your coded message is {}'.format(new_message_str))
            print('give your friend this info:')
            print('message: {}\ncode: {}'.format(new_message_str, self.key))
        return new_message_str
        
    def decode(self):
        message = list(self.message)
        new_message = []
        new_message_str = ''
        
        for i in range(len(message)):
            for l in range(len(self.abcs)):
                if self.abcs[l] == message[i]:
                    try:
                        new_message.append(self.abcs[l - self.key])
                    except:
                        pass
        
        for item in new_message:
            new_message_str += item
        
        if self.print_info:
            print('your decoded message is {}'.format(new_message_str))
        return new_message_str

code = coderDecoder()
code_decode = input('Would you like to code or decode?')
if code_decode == 'code':
    code.code()
elif code_decode == 'decode':
    code.decode()
