# Summarizer

import Algorithmia

input = 'With Amazon Lex, you can build, test, and deploy your chatbots directly from the Amazon Lex console. Amazon Lex enables you to easily publish your voice or text chatbots to mobile devices, web apps, and chat services such as Facebook Messenger, Slack, and Twilio SMS. Once published, your Amazon Lex bot processes voice or text input in conversation with your end-users. Amazon Lex is a fully managed service so as your user engagement increases, you don’t need to worry about provisioning hardware and managing infrastructure to power your bot experience.'
client = Algorithmia.client('simNjBefAAP0jc1S8UIniEnh7381')
algo = client.algo('nlp/Summarizer/0.1.6')
print(algo.pipe(input))
