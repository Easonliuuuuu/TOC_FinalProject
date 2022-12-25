from transitions.extensions import GraphMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
import pandas as pd

# global variable
selection = 0
language = ''
height = 0
weight = 0

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # user start
    def is_going_to_input_language(self, event):
        text = event.message.text
        return text.lower() == 'search'

    def on_enter_input_language(self, event):
        title = 'Meme language selection'
        text = 'Choose between "Chinese" or "English"'
        btn = [
            MessageTemplateAction(
                label = 'Chinese',
                text ='Chinese'
            ),
            MessageTemplateAction(
                label = 'English',
                text = 'English'
            ),
        ]
        url = 'https://i.imgur.com/bCBt6ga.jpeg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_input_select(self, event):
        global language
        text = event.message.text

        if text == 'Chinese':
            language = 'Chinese'
            return True
        elif text == 'English':
            language = 'English'
            return True
        return False

    def on_enter_input_select(self, event):
        send_text_message(event.reply_token, 'Type "1" for general memes. Type "2" for copypastas. Type "3" for jokes.')

    def is_going_to_input_num(self, event):
        global selection
        text = event.message.text

        if text.lower().isnumeric():
            selection = int(text)
            return True
        return False

    def on_enter_input_num(self, event):
        send_text_message(event.reply_token, 'Enter a number between 1~10')

    def is_going_to_input_check(self, event):
        global height
        text = event.message.text

        if text.lower().isnumeric():
            height = int(text)
            return True
        return False

    def on_enter_input_check(self, event):
        text = event.message.text
        if(text == '1' and language == 'English' and selection == 1):
         url = 'https://i.imgur.com/8nLFCVP.png'
         send_image_message(event.reply_token, url)
        elif(text == '2' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/70zdjiilli351.jpg?width=640&crop=smart&auto=webp&s=0d49790c96f28fd1436d39eaf6b6c9502fbf40ff'
            send_image_message(event.reply_token, url)
        elif(text == '3' and language == 'English' and selection == 1):
            url = 'https://external-preview.redd.it/wHP3JyFg8SVTsvZJCi36tMWUCYj_2f30LriRuVvD7wc.png?width=640&crop=smart&auto=webp&s=a8b33707460276faa7768d40d8e00ddf82c03d24'
            send_image_message(event.reply_token, url)
        elif(text == '4' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/dyecygddx4i51.jpg?width=640&crop=smart&auto=webp&s=21d033b67e158c661ecb3c2658d0ea025706f435'
            send_image_message(event.reply_token, url)
        elif(text == '5' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/emn90d5nbqn51.jpg?width=640&crop=smart&auto=webp&s=2c40d34f2d79e88ddae7364735e04097379fb352'
            send_image_message(event.reply_token, url)
        elif(text == '6' and language == 'English' and selection == 1):
            url = 'https://external-preview.redd.it/FbwVy7ZH6hhq6rnutPjwXJdtAis9MNuqFSC7jBRaLWs.jpg?width=640&crop=smart&auto=webp&s=8b159b691b046f3d01727eb24bc3616b439096e0'
            send_image_message(event.reply_token, url)
        elif(text == '7' and language == 'English' and selection == 1):
            url = 'https://i.redd.it/7ux0uk3llrc51.jpg'
            send_image_message(event.reply_token, url)
        elif(text == '8' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/uqh27jjj8bu61.jpg?width=640&crop=smart&auto=webp&s=4bb520cb2a3ee11d8e0236128fcc61de01617cc8'
            send_image_message(event.reply_token, url)
        elif(text == '9' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/nrj9smsfek951.jpg?width=640&crop=smart&auto=webp&s=7f0779e40690624d2a9317c2c503b5ed7e4e1972'
            send_image_message(event.reply_token, url)
        elif(text == '10' and language == 'English' and selection == 1):
            url = 'https://preview.redd.it/wdgjpcm6v5t61.jpg?width=640&crop=smart&auto=webp&s=bd5cb42da1ac3aabd4dc5464264cc10b17b43c01'
            send_image_message(event.reply_token, url)
        elif(text == '1' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'Number one. Steady hand. One day, Kim Jong Un need new heart. I do operation. But mistake! Kim Jong Un die! SSD very mad! I hide fishing boat, come to America. No English, no food, no money. Darryl give me job. Now I have house, American car and new woman. Darryl save life.My big secret. I kill Kim Jong Un on purpose. I good surgeon. The best!')
        elif(text == '2' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'Today when I walked into my economics class I saw something I dread every time I close my eyes. Someone had brought their new gaming laptop to class. The Forklift he used to bring it was still running idle at the back. I started sweating as I sat down and gazed over at the 700lb beast that was his laptop. He had already reinforced his desk with steel support beams and was in the process of finding an outlet for a power cable thicker than Amy Schumers thigh. I start shaking. I keep telling myself I am going to be alright and that there is nothing to worry about. He somehow finds a fucking outlet. Tears are running down my cheeks as I send my last texts to my family saying I love them. The teacher starts the lecture, and the student turns his laptop on. The colored lights on his RGB Backlit keyboard flare to life like a nuclear flash, and a deep humming fills my ears and shakes my very soul. The entire city power grid goes dark. The classroom begins to shake as the massive fans begin to spin. In mere seconds my world has gone from vibrant life, to a dark, earth shattering void where my body is getting torn apart by the 150mph gale force winds and the 500 decibel groan of the cooling fans. As my body finally surrenders, I weep, as my school and my city go under. I fucking hate gaming laptops.')
        elif(text == '3' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'Wowwwww, you meow like a cat! That means you are one, right? Shut the fuck up. If you really want to be put on a leash and treated like a domestic animal then that’s called a fetish, not “quirky” or “cute”. What part of you seriously thinks that any part of acting like a feline establishes a reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to resort to shitty representations of cats to create an illusion of meaning in your worthless life? Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution to your false sense of personality, such as intelligence or charisma in any form or shape. Where do you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely sympathetic towards you as your only escape from the worthless thing you call your existence is to pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant trait, mainly because personality traits require an initial personality to lay their foundation on. You’re not worthy of anybody’s time, so go fuck off, “cat-girl”.')
        elif(text == '4' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'If you shit in the sink at exactly 4:20 am and yell “amogus” 69 times,a shadowy figured called mom will come to beat you up and you will wake up in a place called the orphanage')
        elif(text == '5' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'The Girl you just called fat? She shit herself & lost 15kgs. The Boy you just called stupid? He shit himself. The Girl you just called ugly? She spends hours shitting and farting. The Boy you just tripped? He shit his pants. There`s more to people than you think. Like this if your against bullying.')
        elif(text == '6' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'I sexually Identify as the "I sexually identify as an attack helicopter" joke. Ever since I was a child, I have dreamed of flippantly dismissing any concepts or discussions regarding gender that do not fit in with what I learned in 8th grade bio. People say to me that this joke has not been funny since 2014 and please at least come up with a new one, but I dont care, Im hilarious. Im having a plastic surgeon install Ctrl, C, and V keys on my body. From now on I want you guys to call me "epic kek dank meme trannies owned with facts and logic" and respect my right to shit up social media. If you cant accept me you are a memeophobe and need to check your ability-to-critically-think privilege. Thank you for being so understanding.')
        elif(text == '7' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'So I was waiting in line to vote when all of a sudden this voting "official" came up to me and said that there was something wrong with my voter registration and asked me to follow him to the back. When we went around back he said that I had to take off my pants and show my cock because penis size is the most accurate way to confirm voter identity. Because I thought he was a voting official I swiftly removed my pants and underwear to show him my member. After he fondled it for a bit he said it was good and I could go back into the line. It was only after I voted I realized that he forgot to check my balls too!!! He was obviously not certified to check such an area and I immediately contacted the security guards about his presence. Please do not fall for any tricks like I did! stay safe and happy voting!')
        elif(text == '8' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Who asked (Feat: No one) ───────────⚪────── ◄◄⠀▐▐ ⠀►► 5:12/ 7:𝟻𝟼 ───○ 🔊⠀ ᴴᴰ ⚙️')
        elif(text == '9' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'Shots 1-5: Clearly missed.Shots 6-9: Missed due to recoil (bad spray control).Shots 10-11: Very close, but recoil and inaccuracy make these reasonable misses.Shot 12: Likely didnt actually fire because Hiko was already dead.')
        elif(text == '10' and language == 'English' and selection == 2):
            send_text_message(event.reply_token, 'Sigma male schedule 2:00 am- Wake up 2.05am-Cold shower 2.15am-breakfast,almonds, breast milk bought off Facebook, 50mg adderall 2:30am- begin workout,incline bench 2 plates,12x12 with 30 seconds of rest, no warmup. 2:45am-edging,4hrs (for disipline) 6:45am-cold shower 7:00am-begin sprint to work 8:00am-arrive at work 8:05am-get called into boss office 8:06am-get fired from job for "repeated inappropriate comments" and "predatory behaviour"8:10am-sprint back home9:10am- lunch-raw cod, berries foraged on the way home, small pebbles (for digestion),50mg of adderal 9:10am-edging(as punishment) 3:00pm- bed time')
        elif(text == '1' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'What’s the difference between a police officer and a bullet? When a bullet kills someone else, you know it’s been fired')
        elif(text == '2' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'A male whale and a female whale were swimming off the coast of Japan when they noticed a whaling ship. The male whale recognized it as the same ship that had harpooned his father many years earlier. He said to the female whale, "Lets both swim under the ship and blow out of our air holes at the same time and it should cause the ship to turn over and sink." They tried it and sure enough, the ship turned over and quickly sank.Soon however, the whales realized the sailors had jumped overboard and were swimming to the safety of shore. The male was enraged that they were going to get away and told the female, "Let us swim after them and gobble them up before they reach the shore." At this point, he realized the female was becoming reluctant to follow him. "Look," she said, "I went along with the blow job, but I absolutely refuse to swallow the seamen."')
        elif(text == '3' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'What is the most expensive video-streaming service at this time? College')
        elif(text == '4' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'What has 4 letters, sometimes 9 letters, but never has 5 letters. Just a hint: I did not ask a question.')
        elif(text == '5' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.')
        elif(text == '6' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'A bear walks into a bar and says, “Give me a whiskey and … cola.” “Whythe big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”')
        elif(text == '7' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'Why don’t scientists trust atoms? Because they make up everything.')       
        elif(text == '8' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'What did the fish say when he swam into a wall?  Dam.')        
        elif(text == '9' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'Why did an old man fall in a well? Because he couldn’t see that well!')        
        elif(text == '10' and language == 'English' and selection == 3):
            send_text_message(event.reply_token,'What did one plate say to the other? Dinner is on me!')
        elif(text == '1' and language == 'Chinese' and selection == 1):
            url = 'https://megapx-assets.dcard.tw/images/b96dc903-4258-4c14-b012-2d88a2e41d39/640.webp'
            send_image_message(event.reply_token, url)                   
        elif(text == '2' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/321670978_5999139623440133_2411137264116144546_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=kD8J9o66mawAX_jqmZe&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfBKnfpDThZzYozurYvWNemurXBa1J1I0K6iQ_p2ruddSQ&oe=63AD2281'
            send_image_message(event.reply_token, url)        
        elif(text == '3' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/320707143_1823093314715759_4367062380039821267_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=rAXcE4uxXGIAX_Us8jK&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfCxkE8X19N5NVekZ1VUGEsYwFgLfS6Z7esEugbXm3uO8A&oe=63AD0381'
            send_image_message(event.reply_token, url)        
        elif(text == '4' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/320607233_711343647074356_9060577282553344010_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=48-_Sc1ApjQAX-8_hAR&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfC6kV53-R9yz3f7dooRhUiAtCq192m7Q5ZerrukQILOlA&oe=63AD9829'
            send_image_message(event.reply_token, url)        
        elif(text == '5' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/320172285_2270644039784065_2644979776260774128_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=730e14&_nc_ohc=AeXlj6W4zxIAX8WTFDv&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfC4_3wKVxX1D2lMXmTVgS6psCoPmQUsDQ9TvLtIt-LiEQ&oe=63AD7C68'
            send_image_message(event.reply_token, url)        
        elif(text == '6' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/319238152_1905074963176205_5577722546898830358_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_ohc=F3b4O8izXSwAX_M5K1I&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfAt5ETLSnzg3skwMnuiE9dAcpPbcBAITW4b_mNx-771Ng&oe=63ACBD8C'
            send_image_message(event.reply_token, url)        
        elif(text == '7' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/319116256_920938342178588_8790933479109214991_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=4q2DVJUj__UAX9rYssx&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfAOjBahGjAgoXL--y4ZFoA9TAWymRA7AGhblkW77iLCsw&oe=63AE0806'
            send_image_message(event.reply_token, url)        
        elif(text == '8' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/318735850_513619993858945_8869952728380818499_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=PN2kf59P6lAAX83Xk2l&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfB6RTYsGTsHAoaCThYDNIHTfIuutY3OmuDZdqKTga04FA&oe=63AD9F0C'
            send_image_message(event.reply_token, url)        
        elif(text == '9' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/318457735_519809760181739_2778969541054163616_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=Bz6S8YI8tPAAX_4RQi6&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfBoQ2FZrlJuNmO3dLX7K-COHqapZ91Oi0TlJRn2oc38CQ&oe=63AE8042'
            send_image_message(event.reply_token, url)        
        elif(text == '10' and language == 'Chinese' and selection == 1):
            url = 'https://scontent.fkhh5-1.fna.fbcdn.net/v/t39.30808-6/319135129_518780860284629_819195836084625412_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_ohc=hvYeIWBYBioAX_FLIpw&_nc_ht=scontent.fkhh5-1.fna&oh=00_AfBwIfH63GI1qgA_pLM-Ub6aCnYW1OoyrVrEWzjEt8c1Pw&oe=63ADF143'
            send_image_message(event.reply_token, url)        
        elif(text == '1' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '我朋友整天把台大掛嘴邊，後來被外商相中，現在在家樂福電器部門工作，每天跟客人介紹「這台大冰箱很棒」「這台大電視很讚」')        
        elif(text == '2' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '我代表 馬來西亞，新加坡，印尼，汶萊，東帝汶，菲律賓，緬甸，泰國，越南，竂國，中國，香港，台灣，日本，韓國，朝鮮，印度，孟加拉，巴基斯坦，不丹，巴林，伊朗，伊拉克，阿富汗，斜利亞，沙地阿拉伯，烏茲別克，土耳其，俄羅斯，波蘭，捷克，羅馬尼亞，保加利亞，哈薩克，阿塞拜彊，德國，法國，英國，荷蘭，比利時，西班牙，葡萄牙，愛爾蘭，北愛爾亞，蘇格蘭，冰島，丹麥，瑞典，瑞士，希臘，芬蘭，克羅地亞，意大利，格魯吉亞，亞美尼亞，匈牙利，法羅群島，塞爾維亞，烏克蘭，斯洛文尼亞，斯洛伐克，奧地利，黑山，立陶宛，馬其頓，白俄羅斯，關島，阿聯酋，馬爾代夫，卡塔爾，也門，咯麥龍，尼日利亞，象牙海岸，馬里，加納，埃及，摩納哥，突尼西亞，紐西蘭，美國，加拿大，巴拿馬，哥斯達黎加，秘魯，智利，玻利維亞，委內瑞拉，墨西哥，巴拉圭，烏拉圭，古巴，海地，厄瓜多爾，巴西，阿根廷人，我爺爺，奶奶，姥爺，媽媽，爸爸，姥姥，外婆，太姥姥，姥爺，姑奶奶，姑爺，大爺，三爺，大奶奶，三奶奶，姨奶奶，姨爺，舅爺，舅奶奶，姑姥姥，姨姥爺，舅姥爺，舅姥姥，伯伯，二伯，三伯，伯母，叔叔，二叔，三叔，嬸嬸，二嬸，三嬸，姑姑，大姑，二姑，姑父，大姑父，二姑父，三姑父，舅舅，大舅，二舅，小舅，舅媽，大舅媽，二舅媽，舅媽，姨，大姨，小姨，三姨，姨父，大姨夫，小姨夫，三姨夫，堂兄，堂弟，堂姐，堂妹，表哥，大表哥，二表哥，小表哥，表弟，一二三四五六七八表弟，表姐，表妹，姨哥，姨姐，姨弟，姨妹，嫂子，弟妹，弟弟，表弟妹，姐夫，表姐夫，妹夫，侄子，侄女，外甥，外甥女，大伯子，大伯娘，小叔子，小嬸子，大姑子，小姑子，大舅子，大妗子，小舅子，小妗子，大姨子，小姨子，公公，婆婆，岳飛，岳父，岳母，劉備，關羽，張飛，趙雲，馬超，諸葛亮，黃忠，魏延，龐統，關平，周倉，廖化，劉封，糜芳，傅士仁，王平，張翼，馬謖，孫乾，孟獲，劉禪，姜維，蔣琬，馬岱，夏侯霸，嚴顏，徐庶，糜夫人，關興，張苞，馬良，伊籍，諸葛瞻，諸葛尚，傅儉，沙摩柯，曹操，曹丕，曹植，曹真，曹昂，曹安民，曹髦，曹芳，夏侯淵，徐晃，張遼，許褚，典韋，夏侯惇，張頜，司馬懿，司馬昭，司馬師，司馬炎，龐德，荀賎，郭嘉，李典，樂進，曹洪，鄧艾，鐘會，曹仁，荀攸，程立，李恢，楊修，郭淮，文聘，焦觸，於禁，孫權，孫策，孫堅，黃蓋，甘寧，周瑜，程普，韓當，太史慈，周泰，呂蒙，陸遜，朱然，潘璋，馬忠，陳武，董襲，張昭，濰翻，魯肅，丁奉，淩統，孫尚香，董卓，呂布，貂蟬，高順，陳宮，宋憲，魏續，李儒，袁紹，袁尚，袁術，袁熙，顏良文醜，高覽，田豐，審配，劉表，劉琦，蔡瑁，張允，霍駿，黃祖，呂公，馬騰，韓遂，馬鐵，何進，宋江，盧俊義，吳用，公孫勝，關勝，林沖，秦明，呼延灼，花榮，柴進，李應，朱仝，魯智深，武松，董平，張清，楊志，徐寧，索超，戴宗，劉唐，李逵，史進，穆弘，雷橫，李俊，阮小二，張橫，阮小五， 張順，阮小七，楊雄，石秀，解珍， 解寶，燕青，朱武，黃信，孫立，宣讚，郝思文，韓滔，彭玘，單廷珪，魏定國，蕭讓，裴宣，歐鵬，鄧飛， 燕順，楊林，淩振，蔣敬，呂方，郭 盛，安道全，皇甫端，王英，扈三娘，鮑旭，樊瑞，孔明，孔亮，項充，李袞，金大堅，馬麟，童威，童猛，孟康，侯健，陳達，楊春，鄭天壽，陶宗旺，宋清，樂和，龔旺，丁得孫，穆春，曹正，宋萬，杜遷，薛永，施恩，周通，李忠，小橘子，白勇太，馬特，鏡，西澤爾，雷因，穆尼克拉，實驗體 7 號，神風玉堂，雙生戰神，永夜君主，火線追擊，迅捷流星，星空獵手，S - 追光者，S - 逐星者，S - 破曉者，S - 裁決者，S - 烈魂者，赤橙夢魘，指揮官SPX，勞斯萊斯QEX，極音戰歌，紫鏡之顛，擎天雷諾，天蓬，晶耀之星，滄海，聖金獅王，驚鴻，幻影戰神，天啟，地獄天啟，勁霸，極光，銀河戰艦，玄武，金刃黃蜂，超能橘貓，極夜幽冥，天使之翼，動感熊貓，沙漠領主，夜雷戰神，凌霜風暴，燃魂針尖，雷霆風暴，風暴剃刀，飛躍，光電遊俠，獵影，極地戰甲，利刃，剃刀，1 週年剃刀，襲影，甜蜜旋風，紫電，白馬王子，優格大巴，攝魂，寒凌，飛天，SPEED86，噴焰新星，深海狂鯊，金甲戰狼，極鼠先鋒，東方限定 • 大黃蜂，綠茵前鋒，藍色脈衝，紫爵，玫翼，白鴿，暴風勇士，K24，大 Q 巴，愛神之心，愛神之吻，刺客，挑戰者，南瓜車，甜心號，橘神風暴，越野者，暴君，小哈，新手賽車，熱血青銅 III，熱血青銅 II，熱血青銅 I，迅捷白銀 III，迅捷白銀 II，迅捷白銀 I，疾風黃金 IV，疾風黃金 III，疾風黃金 II，疾風黃金 I，幻影鉑金 V，幻影鉑金 III，幻影鉑金 II，幻影鉑金 I，流星鑽石 V，流星鑽石 IV，流星鑽石 III，流星鑽石 II，流星鑽石 I，絕影星耀 V，絕影星耀 IV，絕影星耀 III，絕影星耀 II，絕影星耀 I，最強車神，傳奇車神，雷震子，哪吒，星夢精靈，幻影戰龍，逆天鷹，仙靈鶴，企鵝仔仔，企鵝囡囡，正義熊貓，火麒麟，聖光雪狐，白熊，雪域獅王，鹿力大仙，羊力大仙，虎力大仙，彩虹獨角獸，雪萌寶寶，小白龍，白澤，美人魚，無常小黑，無常小白，小竹鼠，探險鴨，狂想曲，躍進者，小海豹，怪獸，東方限定 • 赤速，水槍騎兵，熱血衝鋒，極速衝鋒，1 週年雄獅，1 週年紀念，新手滑板，福鼠2020，東方限定 • 飛馳，炫動SPEED，中國城，老街管道，情迷愛琴海，玫瑰之戀，法老金字塔，冰川滑雪場，11 城，反向 11 城，龍門新春，廣寒仙境，城市網咖，因特拉肯，小豬部落，希臘神殿，水行瑪雅，雪地大冒險，洛杉磯，情迷法蘭西，時之沙，星星火車站，彩虹風車島，反向彩虹風車島，龍騰燈海，北海漁場，繁花巴比倫，夜鳴沙都，TROY - 熔煉車間，電音夢工場，幻音城假日，320 冒險島，冰雪企鵝島，西湖，桃園劍閣，TROY - 零號試驗場，一號公路，秋之物語，長城，人魚島探險，莫高窟，亞特蘭提斯，反向亞特蘭提斯，秋名山，美洲大峽谷，極速空港，超級起步，斷鳥起步，斷痕起步，空噴，落地噴，雙噴，斷位飄移，斷位雙噴，甩尾飄移，甩尾斷痕，雙煞斷氮，側身飄移，CW噴，WCW噴，CWW噴，WCWW噴，WWC起步，小飄雙噴，氮氣延續，停滯飄移，進階氮氣出彎，側身進階，甩尾進階，暴力氮氣入彎，單段進階，彈射甩尾，U甩，雙煞彈射，雙煞U甩，輕煞彈射，小飄雙煞CWW 告訴你：這到底殺毀')            
        elif(text == '3' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '笑死幹😄台大死讀書仔 出社會還不是領22k 😂😂我讀高職就翹課跟師傅修車 🔧一堆人看不起我們做黑手的🤣🤣跟你說我們雖然沒有讀什麼書😅😅但是等你畢業我至少一個月70k 起跳啦😎😎最看不起這種學歷優越猴了🐒😠還不是一堆生活白癡🤣🤣')            
        elif(text == '4' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '我有憂鬱症！我！有！憂！鬱！症！！！！媽的聽不懂憂、鬱、症這三個字是要我用美工刀寫給你看嗎！！！！！！！！是憂鬱症讓我出軌的！！！！我很愛他好嗎！！！！！！！！！不要在說什麼出軌就是我的錯了！！！不是我願意的呀！！！！！Not I wanted！！！！！！罵三小淦誰在用怒洗我的版誰就準備去死啦！！淦紺榦汵凎倝！！！！！我要發瘋了我真的要發瘋了我要瘋了！！！！有憂鬱症就夠、夠幸苦了，還要被你們這群鍵盤殺人魔不停殺我！！！！！贛我真的要崩潰了讓我去死啦贑淦簳！！！！！！肏你嗎！？！！！！FUCK！！SHIT！！！！！GOD DAMN！！！！！！！！！靠北！！！！！！！！八嘎鴨洛！！！！！！！！！！！崩潰到快把世上所有髒話都罵出來、艮拎辣啊啊啦！拎ㄋㄧㄚˊ、、、若有人傳不實謠言不排除提告')            
        elif(text == '5' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '愛的OOO同學,根據校園網路後台數據顯示:在2021年9月9日至2021年9月24日期間內你共使用校園網路帳號瀏覽色情網頁134次,嚴重違反國立OO大學《學生網絡安全準則》。大學生當前應以學業為重,為了規範你的平時行為,請你於2021年9月27日7:40至生輔組報到,進行網絡安全與健康教育講座。並在講座之後向導師提交2000字心得體驗,截止時間2021年9日28日·青少年應以學習為重,希望你能深刻檢討,吸取教訓,規範自己以後的行為,健康上網。[電算中心]')            
        elif(text == '6' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '看完樓主的這個帖子以後,我的心久久不能平靜,正有如滔滔江水綿延不覺有如黃河氾濫一發不可收拾阿真是為之震撼啊!為什麼會有如此好的帖子呢?我縱橫網絡多年,自以為再也不會有任何帖子能打動我那激昂的心,沒想到今天看到了如此精妙絕倫的這樣一篇帖子.板主,是你讓我深深地理解了人外有人,天外有天,強中自有強中手,一山還有一山高這句話.謝謝你!在看完這帖子以後,我沒有立即回复,因為我生怕我那庸俗不堪知識淺薄的低賤回覆會玷污了這網上少有且石破天驚為之震撼人心世道的帖子.但是我還是回覆了,因為我覺得如果不能在這如此精彩完美的帖子上面留下自己的那心中的浩大波滔,那我死也不會瞑目的!能夠在如此精彩的帖子上面留下在下的渺小卑微的見解和賤名是多麼驕傲多麼光榮的一件事啊!板主,請原諒我的自私自利!請原諒我的不才之恥,我知道無論用多麼華麗燦爛的詞彙和辭藻來形容板主您帖子的精彩程度都是不夠的,都是虛偽的,所以我只想說一句:您的帖子真的是太好了!我願意一輩子的看下去!這篇帖子構思新穎,題材獨具匠心,文章段落清晰,情節豐富詭異,故事跌宕起伏,段落主線分明,劇情引人入勝,文學更是中流砥柱,平淡中顯示出不凡且帶有文學性的藝術氣息,可謂是字字珠璣,句句經典,是我輩應當學習之典範,效法之模範,揣摩之楷模,以小說藝術的角度而言,這篇帖子可能不算太成功,但它的實驗意義卻遠遠大於成功本身.正所謂:"一馬奔騰,射雕引弓,天地都在我心中!"板主真不愧為無厘界新一代的開山祖師!本來我已經對這個dcard的文章徹徹底底失望了,覺得這個dcard已經在也沒有前途了,心裡充滿了無盡的悲傷和感慨.但是看了你的這個帖子以後,又讓我對dcard產生了如曙光般的希望.是你讓我的心裡重新燃起希望的火炬,是你讓我的心死灰復燃,是你拯救了我那一顆早已凍結的心!本來我決定不會在dcard回任何的帖子了,但是看了你的帖子,我告訴自己這個帖子是一定要回的!這是百年難得一見的好帖啊!蒼天有眼啊,讓我在有生之年得以觀得如此精彩絕倫的帖子!板主的話真如"大音希聲掃陰翳",猶如"撥開雲霧見青天",使我等網民看到了希望,看到了未來!晴天霹靂,醍醐灌頂或許不足以形容大師文章的萬一;巫山行雲,長江流水更難以比擬大師的文才!黃鐘大呂,振聾發聵!你燭照天下,明見萬里;雨露蒼生,澤被萬方!透過你深邃的文字,我彷彿看到了你鷹視狼顧,龍行虎步的偉岸英姿;彷彿看到了你手執如椽大筆,寫天下文章的智慧神態;彷彿看見了你按劍四顧,江山無數的英武氣概!樓主,你說的多好啊!我在dcard打滾這麼多年,所謂閱人無數,見怪不怪了,但一看到樓主的氣勢,我就覺得板主同在dcard裡灌水的那幫小混蛋有著本質的差別,那憂鬱的語調,那熟悉的簽名,還有字裡行間高屋建瓴的辭藻.沒用的,板主,就算你怎麼換馬甲都是沒有用的,你的億萬擁戴者早已經把你認出來了,你一定就是傳說中的最強id.自從dcard改版之後,我就已經心灰意冷,對社區也沒抱什麼希望了,傳說已經幻滅,神話已經終結,留在dcard還有什麼意思.沒想到,沒想到,今天可以再睹樓主的風範,我激動得忍不住就在屏幕前流下了眼淚.是啊,只要在板主的帶領下, 就有希望了.我的內心再一次沸騰了,我胸腔裡的血再一次燃燒了.板主的話概括扼要,一語道出了我們苦想多年的而不可得答案的幾個重大問題的根本.板主就好比dcard的火炬,板主就好比dcard的燈塔,板主就好比dcard的棟樑.有板主在, dcard的明天必將更好!板主你的高尚情操太讓人感動了.在現在這樣一個物慾橫流的金錢社會裡,竟然還能見到板主這樣江湖少見的性情中人,無疑是我這輩子最大的幸運.讓我深深感受到了人性的偉大.板主的帖子,就好比黑暗中刺裂夜空的閃電,又好比撕開烏雲的陽光,一瞬間就讓我如飲甘露,讓我明白了永恆的真理在這個世界上是真實存在著的.只有樓主這樣具備廣闊胸懷和完整知識體系的人,才能作為這真理的唯一引言者.看了板主的帖子,讓我陷入了嚴肅的思考中,我認為,如果不把板主的帖子頂上去,就是對真理的一種背叛,就是對謬論的極大妥協.因此,我決定義無返顧的頂了!樓主,在遇到你之前,我對人世間是否有真正的聖人是懷疑的;而現在,我終於相信了!我曾經忘情於漢廷的歌賦,我曾經驚訝於李杜的詩才,我曾經流連於宋元的詞曲;但現在,我才知道我有多麼淺薄!樓主的帖子實在是寫得太好了.文筆流暢,修辭得體,深得魏晉諸朝遺風,更將唐風宋骨發揚得入木三分,能在有生之年看見樓主的這個帖子.實在是我三生之幸啊.看完樓主的這個帖子之後,我竟感發生出一種無以名之的悲痛感──啊,這麼好的帖子,如果將來我再也看不到了,那我該怎麼辦?那我該怎麼辦?直到我毫不猶豫的把樓主的這個帖子收藏了,我內心的那種激動才逐漸平復下來.可是我立刻想到,這麼好的帖子,倘若別人看不到,那麼不是浪費樓主的心血嗎?經過痛苦的思想鬥爭,我終於下定決心,我要把這個帖子一直往上頂,往上頂到所有人都看到為止!我現在終於明白我缺乏的是什麼了,正是樓主那種對真理的執著追求和樓主那種對理想的艱苦實踐所產生的厚重感.面對樓主的帖子,我震驚得幾乎不能動彈了,樓主那種裂紙欲出的大手筆,竟使我忍不住一次次的翻開樓主的帖子,每看一次,讚賞之情就激長數分,我總在想,是否有神靈活在它靈秀的外表下,以至能使人三月不知肉味,使人有餘音穿梁,三日不絕的感受.樓主,你寫得實在是太好了!我唯一能做的,就只有把這個帖子頂上去這件事了.樓主,我支持您!！ ！ ~！哥並不為樓主的標題所吸引，也不是被貼子的內容所迷惑。哥不是來搶沙發的，也不是來打醬油的。哥不是來為樓主吶喊加油的，也不是對樓主進行圍堵攻擊的。哥只是為了十萬積分默默奮鬥你是個美女，哥毫不關心； 你是個怪獸，哥絕不在意；你是個帥哥，哥不會嫉妒；你是個畜男哥也不會鄙視。你的情操再怎麼高尚，哥也不會讚美; 你的道德如何淪喪，哥也不為所動。在這個處處都要驗證碼的時代，不得不弄個會員來噹噹之前也是每天看貼無數,基本上不回貼. 後來發現這樣很傻,很多比哥註冊晚的人級別都比我高,但是不管妳是什麼或者什麼都不是,哥已經覺悟到自己的渺小之卑微,給大爺跪了')    
        elif(text == '7' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '你好，你好吗，我喜欢你的帖子，他们很有趣，如果我们是朋友，我将不胜感激我向你发送了一个朋友请求，但它从未奏效，如果你不介意，请尝试从你的 Facebook 成为朋友。 非常感谢')            
        elif(text == '8' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '女大十一變女大十一變 女大十一變一十大女變\n一十大女變一十大女變一十大女變一十大女變\n一十大女變一十大女變其實字都一樣但看起來就是斜的')            
        elif(text == '9' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '超好笑？你為什麼要笑？你憑什麼笑？我就這麼好笑嗎？我明白了，一直以來我就是你的陪襯品，我就是一個小丑一個玩偶。我累了我累了真的累了，沒有人能懂我，沒人能理解我面具下的脆弱，破防了我真的破防了。你覺得我很可憐是吧，我不需要的你的同情，把你那虛偽的面容藏好，我是嬌貴的蝴蝶，是滴血的玫瑰，我就是我，是不一樣的彩虹。')            
        elif(text == '10' and language == 'Chinese' and selection == 2):
            send_text_message(event.reply_token, '幫我做直播  拿著 照我 師傅確定要拍嗎? 確定要拍嗎? 我中了兩槍....希望大家 如果我這一次不幸死的話 請大家一定要傳承我的精神一定要傳承我的精神  啊啊啊啊啊啊啊啊 請大家照顧我的老婆跟小孩拜託大家 拜託大家還有我的媽媽 拜託大家  啊啊啊啊啊啊啊啊')           
        elif(text == '1' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '學海無涯，回頭是岸')          
        elif(text == '2' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '我：醫生，我手術後要多久才能拉小提琴？醫生：一個月。我：謝謝你，我本來不會拉的！')        
        elif(text == '3' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '媽媽: 小陳! 不可以用手指月亮。 小東: 蛤?')        
        elif(text == '4' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '我跟你們說一件事實 兩件80')        
        elif(text == '5' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '曹操字孟德 劉備字玄德 伍佰勒？ 五百字心得')        
        elif(text == '6' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '有一天伍佰打了玖哲一下，他就變成四百五了')       
        elif(text == '7' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '栗子從山上滾下來變什麼？ 血淋淋的栗子')        
        elif(text == '8' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '葡萄點名 葡萄柚')        
        elif(text == '9' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '白氣球揍了黑氣球一拳黑氣球很痛很生氣於是決定 告白氣球')        
        elif(text == '10' and language == 'Chinese' and selection == 3):
            send_text_message(event.reply_token, '為什麼超人要穿緊身衣？ 因為救人要緊')        
        send_text_message(event.reply_token, '請輸入您的體(整數)')

    def is_going_to_send(self, event):
        global weight
        text = event.message.text

        if text.lower().isnumeric():
            weight = int(text)
            return True
        return False

    

