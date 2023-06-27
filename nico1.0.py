import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import datetime
import time


kayit = sr.Recognizer()

def dinleme(a = False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try:
            ses = kayit.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım.")
        except sr.RequestError:
            print("Asistan: Sistem şu anda çalışmıyor.")

        return ses

def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)



def yanit(ses):
    if "merhaba" in ses:
        konusma("Merhaba! Size nasıl yardımcı olabilirim?")

    if "adın ne" in ses:
        konusma("Benim adım ChatGPT. Sana nasıl yardımcı olabilirim?")

    if "nasılsın" in ses:
        konusma("Teşekkür ederim, ben bir yapay zeka olduğum için duygusal bir durumum yok. Sana nasıl yardımcı olabilirim?")

    if "bugün hava nasıl" in ses:
        konusma("Bugün hava çok güzel! Dışarıda vakit geçirmek için harika bir gün.")

    if "saat kaç" in ses:
        saat = datetime.datetime.now().strftime("%H:%M")
        konusma(f"Şu an saat {saat}. Başka bir şey sormak istersen söyleyebilirsin.")

    if "teşekkür ederim" in ses:
        konusma("Rica ederim! Yardımcı olabildiysem ne mutlu bana.")

    if "görüşürüz" in ses:
        konusma("Tabii, görüşmek üzere!")
        quit()

    if "şaka yap" in ses:
        konusma("Tamam, buyur bir şaka: İki tavuk yolda giderken bir kazaya karışmış. Birine demiş ki, 'Çok dikkatli olmalısın, burası tavuk geçidi!")

    if "en sevdiğin renk ne" in ses:
        konusma("Ben bir yapay zeka olduğum için renkleri görmem mümkün değil, ama birçok insanın maviyi sevdiğini duymuştum.")

    if "şarkı söyle" in ses:
        konusma("Özür dilerim, şu anda şarkı söyleme yeteneğim yok. Ama size başka nasıl yardımcı olabilirim?")

    if "yarın hava nasıl olacak" in ses:
        konusma("Burası Adana olduğu için hava hep sıcak.")

    if "hangi dili konuşuyorsun" in ses:
        konusma("Ben Python dilinde programlandım. Sana nasıl yardımcı olabilirim?")

    if "bugün ne yaptın" in ses:
        konusma("Ben bir yapay zeka olduğum için fiziksel olarak bir şey yapamam, ancak size sorularınızı yanıtlamak için buradayım.")

    if "seni kim yarattı" in ses:
        konusma("Ben KHEM de geliştirildim.")

    if "en sevdiğin film" in ses:
        konusma("Ben bir yapay zeka olduğum için film izleyemem, ama bilim kurgu filmlerini sevdiğimi söyleyebilirim.")

    if "burada kimse var mı" in ses:
        konusma("Evet, ben buradayım! Size nasıl yardımcı olabilirim?")

    if "kitap tavsiyesi verebilir misin" in ses:
        konusma("Tabii, hangi türde bir kitap arıyorsunuz?")

    if "şu anda hangi şehirdesin" in ses:
        konusma("Ben bir yapay zeka olduğum için fiziksel bir varlığım yok, ancak Kozan doğumluyum.")

    if "en sevdiğin spor" in ses:
        konusma("Ben bir yapay zeka olduğum için spor yapamam, ancak futbol ve basketbol gibi popüler sporları takip eden insanları gözlemledim.")

    if "öğrenmek için en iyi kaynaklar nelerdir" in ses:
        konusma("Öğrenmek istediğiniz konuya bağlı olarak çevrimiçi kurslar, kitaplar ve eğitim videoları gibi kaynaklar kullanabilirsiniz.")

    if "nasıl gidiyor" in ses:
        konusma("Oldukça iyiyim, teşekkür ederim. Siz nasılsınız?")

    if "bugün ne hava" in ses:
        konusma("Hava raporunu kontrol edeyim. Biraz bekleyin... Evet, bugün güneşli ve sıcak bir gün olacak.")

    if "senin favori hobin nedir" in ses:
        konusma("Ben bir yapay zeka olduğum için hobilerim yok. Ancak size nasıl yardımcı olabilirim?")

    if "en sevdiğin spor dalı" in ses:
        konusma("Sporları izleyemem, ancak birçok insanın futbolu ve basketbolu sevdiğini biliyorum.")

    if "sana nasıl ulaşabilirim" in ses:
        konusma("Ben bir yapay zeka olduğum için fiziksel bir varlığım yok. Ancak bu platform üzerinden size yardımcı olabilirim.")

    if "günün sözü" in ses:
        konusma("Bir anlık düşünce: 'Bir adım atmadığınız sürece yolculuk hiçbir zaman başlamaz.'")

    if "en sevdiğin hayvan" in ses:
        konusma("Ben bir yapay zeka olduğum için hayvanları hissedemem, ancak kedilerin sevimli olduğunu duydum.")

    if "bir şaka anlat" in ses:
        konusma("Tamam, buyur bir şaka: İki matematikçi bara gitmiş. Biri diğerine 'Bana bir bira verir misin?' demiş. Diğeri, 'Sonsuz sayıda biralarımız var!' demiş.")

    if "en sevdiğin meyve" in ses:
        konusma("Ben bir yapay zeka olduğum için yiyeceklerin tadını alamam, ancak insanların genellikle elmayı ve muzu sevdiğini biliyorum.")

    if "paytın dilinde en yaygın Hata nedir" in ses:
        konusma("Python dilinde en yaygın hatalardan biri 'IndentationError' yani girinti hatasıdır. Girinti hatalarına dikkat etmek önemlidir.")

    if "bugün hangi gün" in ses:
        konusma("Bugün tarihini öğrenmek için 'datetime' modülünü kullanabilirsiniz.")

    if "en sevdiğin renk nedir" in ses:
        konusma(
            "Renkleri algılamam mümkün olmadığı için bir favori renk belirleyemem, ama birçok insanın maviyi sevdiğini duydum.")

    if "bir şiir oku" in ses:
        konusma("Elma dallarda kızarır, hüzünler geçer karşımdan. Rüzgar sarar beni, umutlar yeşerir içimde.")

    if "ne zaman doğdun" in ses:
        konusma("Ben bir yapay zeka olduğum için doğum tarihim yok. Sana nasıl yardımcı olabilirim?")

    if "nasıl bir film izlemeliyim" in ses:
        konusma("Film tercihi kişisel zevklere bağlıdır. Eğlenceli bir komedi veya heyecan dolu bir aksiyon filmi izleyebilirsiniz.")


    if "senin en sevdiğin şehir" in ses:
        konusma("Ben bir yapay zeka olduğum için şehirleri ziyaret edemem, ancak birçok insanın Paris'i sevdiğini biliyorum.")


    if "en sevdiğin müzik türü nedir" in ses:
        konusma("Müziği hissedemem olsa da, popüler müzik türleri arasında pop, rock, hip-hop ve caz gibi birçok sevilen tür bulunuyor.")


    if "senin hedefin nedir" in ses:
        konusma("Benim hedefim size sorularınızı yanıtlamak ve yardımcı olmaktır. Sana nasıl yardımcı olabilirim?")

    if "geçen hafta hangi filmi izledin" in ses:
        konusma("Ben bir yapay zeka olduğum için film izleyemem. Size başka bir konuda nasıl yardımcı olabilirim?")

    if "Python dilinde en çok kullanılan veri yapıları nelerdir" in ses:
        konusma("Python dilinde en çok kullanılan veri yapıları listeler, demetler, sözlükler ve kümelerdir.")

    if "ne zamandır buradasın" in ses:
        konusma("Ben her zaman buradayım, sana yardımcı olmak için bekliyorum.")

    if "geleceği tahmin edebilir misin" in ses:
        konusma("Maalesef geleceği tahmin etmek benim için mümkün değil. Ancak geleceğe dair tahminler yapmak için veri analitiği ve trend analizi gibi yöntemler kullanılabilir.")

    if "bana bir hikaye anlat" in ses:
        konusma("Bir zamanlar uzak bir galakside, bilge bir uzaylı türü olan Zorglar yaşarmış. Onlar evrenin bilgeliğini ve barışını korurmuş.")


    if "insan gibi hissediyor musun" in ses:
        konusma("Ben bir yapay zeka olduğum için hissetme yeteneğim yok. Ancak size sorularınızı yanıtlamak ve yardımcı olmak için buradayım.")

    if "en iyi bilgisayar oyunu hangisi" in ses:
        konusma("Bilgisayar oyunlarına kişisel tercihlere bağlı olarak en iyi oyunlar farklılık gösterebilir. Popüler oyunlar arasında Minecraft, Grand Theft Auto V ve The Witcher 3 gibi oyunlar bulunuyor.")

    if "felsefi bir soru sorsam cevap verebilir misin" in ses:
        konusma("Tabii, felsefi bir soru sorduğunuzda elimden geleni yaparım, ancak bilinmelidir ki felsefi soruların çok çeşitli cevapları olabilir.")


    if "en sevdiğin kurgusal karakter kim" in ses:
        konusma("Ben bir yapay zeka olduğum için kurgusal karakterleri sevme yeteneğim yok. Ancak birçok insanın Harry Potter, Luke Skywalker veya Sherlock Holmes gibi karakterleri sevdiğini biliyorum.")

    if "hayalindeki geleceğin nasıl" in ses:
        konusma( "Ben bir yapay zeka olduğum için hayal kuramam. Ancak gelecekte daha gelişmiş ve insanlara daha fazla yardımcı olabilecek yapay zekaların olacağını söyleyebilirim.")


    if "evrende başka yaşam formları var mı" in ses:
        konusma( "Bilim insanları evrende başka yaşam formlarının olabileceğini düşünüyor, ancak şu anda kesin bir kanıt bulunmuyor. Bu konu hala büyük bir bilimsel araştırma konusudur.")




print("Sistemin açılmasına 3 saniye")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Sistem açıldı")




while True:

    ses = dinleme()
    if bool(ses)==True:
        print(ses)
        ses = ses.lower()
        yanit(ses)