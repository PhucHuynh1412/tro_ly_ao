# TODO: Thu vien
import datetime
import playsound
from gtts import gTTS
import speech_recognition as sr 
import os
import webbrowser as wb 


# TODO: Ham
def speak(text):
    print(f"Như: {text}")
    nhu = gTTS(text,lang='vi')
    nhu.save('nhu.mp3')
    playsound.playsound('nhu.mp3')
    os.remove('/home/hltphuc/Lap_trinh/tro_ly_ao/nhu.mp3')

def listen():
    nhu = sr.Recognizer()
    with sr.Microphone() as source: 
        nhu.pause_threshold=1
        audio = nhu.listen(source,phrase_time_limit=7)
        try:
            text = nhu.recognize_google(audio, language='vi-VN')
            print(f"Anh: {text}")
            return text
        except:
            speak("Em nghe không rõ anh nói lại nhen!")
            listen()

def hello():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 10:
        text = "Chào buổi sáng anh yêu ! anh ăn sáng chưa !! nhớ giữ tập thể dục và giữ sức khỏe đó, yêu anh nhiều lắm! "
        speak(text)
    if hour > 10 and hour <= 15:
        text = "Chào anh yêu! anh nhớ nghỉ xíu còn chiều làm đó ! nhớ em không ! hi hi !"
        speak(text)
    if hour > 15 and hour <= 19:
        text = "Chiều nay anh mệt không ! nhớ uống nước nhen ! uống ít nước ngọt thui, dễ bệnh lắm ! thương anh quá à !"
        speak(text)
    if hour > 19 and hour <= 23:
        text = "Tối rồi anh nhớ nghỉ ngơi sớm! đừng làm việc khuya quá ! nhớ em thì ngủ sẽ mơ thấy em mà !! nên ngủ nhen !! thương anh !"
        speak(text)
    if hour > 23 and hour < 5:
        text = "Cục cưng không ngủ được à ! thức khuya chơi game là em giận đó nhen ! còn nhớ em quá thì ngủ đi để mơ thấy em nhen ! thương anh lắm luôn đó !!"
        speak(text)
    speak("Anh cần em giúp gì nè !")

def time(cmd):
    today = datetime.datetime.now()
    text = ""
    if "giờ" in cmd:
        text = f"Anh yêu bây giờ là {today.hour} giờ {today.minute} phút {today.second} giây."
    elif "ngày" in cmd:
        text = f"Anh yêu hôm này là ngày {today.day} tháng {today.month} năm {today.year}"
    speak(text)

def brain(text):
    if 'mấy giờ' in text or 'ngày mấy' in test:
        time(text)

def main():
    hello()
    text = listen().lower()
    brain(text)


if __name__ == "__main__":
    main()

