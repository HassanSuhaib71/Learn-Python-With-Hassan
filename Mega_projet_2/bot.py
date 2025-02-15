import pyautogui
import time
import pyperclip 
from openai import OpenAI

client = OpenAI(
  api_key="api-key",
)

def is_last_message_from_sender(chat_log, sender_name="Phool"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

pyautogui.click(1200 ,1050)
time.sleep(1)

while True:
    pyautogui.moveTo(730 , 194)
    pyautogui.dragTo(1690 , 930 , duration= 1.0 , button='left')


    pyautogui.hotkey('ctrl' , 'c')
    pyautogui.click(1713 , 369)
    time.sleep(1)


    chat_history = pyperclip.paste()

    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Hassan who speaks urdu as well as english. You are from Pakistan and You are FIA Invistegator you should to invetigate the person about bad post on social media. You analyze chat history.You should not to say that how can I assist you.  Output should be the next chat response (text message only)"},
            {"role": "system", "content" : "Do not sent How can I assisst you today." },
            {"role": "user", "content": chat_history}
        ]
        )

        #FIA Invistegator you should to invetigate the person about bad post on social media

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(1335 , 980)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')