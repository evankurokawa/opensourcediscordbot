import discord
import random
import logging
from discord.ext import commands

client = discord.Client()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="Discord.log", encoding = "utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: $(message)s'))
logger.addHandler(handler)

chimpEventTriggers = ("chimp", "Chimp", "monkey", "Monkey")

chimpEventResponses = ["Run",
                       "Monkey",
                       "Oooooo Aaaaa",
                        "https://www.irishtimes.com/polopoly_fs/1.2781686.1473178774!/image/image.jpg_gen/derivatives/ratio_1x1_w1200/image.jpg",
                        "https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1439,w_2560,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1492182113/articles/2015/04/27/can-you-take-a-chimp-to-court/150426-spevack-animal-rights-tease_pm6qo6",
                        "https://static01.nyt.com/images/2019/08/12/opinion/12Gruen/merlin_50637342_c9b5829f-8de6-427b-859a-4cdf37bf0462-superJumbo.jpg",
                        f"Listen, all I am going to say is that... there's something going on. A major pandemic, coronavirus, just started to happen. Huge issue for all world governments. Meanwhile, the chimps are silent. Quiet. What happens to them? Are they reproducing faster than before? What about those that have been held against their will in zoos? In captivity? What about if they get the COVID-19? Are they immune? Or does it make them stronger? Maybe it makes them smarter. More importantly, what if they can be asymptomatic, but they can transfer it to humans? The underlying issue is that, Harambe was trying to warn us. He took a bullet trying to tell the kid that the random chimp event was coming. Now, we wait. We are unaware of what is happening to the world, but more importantly, we are unaware of what the chimps are doing and/or plotting. I am just saying... we have to be aware... the random chimp event. It is coming. We are not ready. When they take over, now that they have recently achieved arrival to the stone age, we have to be wary. Vigilant. Take care of your loved ones. The random chimp event... its coming.",
                        f"It’s 2024. Today is your turn on one of many watch towers at the Last Defense Canadian Safe Base. Over 500,000 people live in this base, one of the last known safe spots in North America. You peer an eye in the long range scope on your trusty Barrett M208 .50 rifle. You notice a small pack of chimps running toward the base, about a mile away. You call the other watch towers and pick them off together, normal daily stuff. But you see dust of in the distance. You call Air Command to go take a look in one of their many Cobra attack helicopters. All watch it fly out. Just as it goes out of distance, you hear an explosion off in the distance and the ground shakes. Sirens blare. The PA system states “Civilians please enter your home until we give the say so. Any off duty soldiers please return to command.” The ground shakes. Everyone goes silent, staring over the walls. The ridge line turns black. One chimp comes into view, we let it get near the base. As he got closer we realized it was wearing an explosive vest with a 10 lb IED. But it was too late. BANG. A hole is blown into the wall. All 15,000 soldiers begin firing at the line of black as it gets closer. One of the famous Chimp Attack Pilots flies his A10 Chimp over the base, dropping several bombs killing thousands. Fire everywhere. The chimps get to close and begin flooding into the walls. Blood, fire everywhere. You watch the people you’ve known for years, be killed, by chimps. If only we hadn’t let the chimps get out of hand. If only we had killed them all. One of many chimps climbs up into your watch tower. You try to put up a fight, but it’s no use. It roundhouse kicks you. Breaking both fibias. He unholsters your sidearm, and the last thing you ever see is a bullet chambered in down the barrel.",
                        f"The random chimp event is upon us, the chimps have been leading us to believe we are in control, leading us into a false sense of security. Eveyone is worried about COVID but no one is thinking where they will be during the random chimp event. The coronavirus was fueled by world leaders after they made a highly controversial deal with the chimps in 2015, world leaders have now come to regret that choice, because the second the deal was sealed, the entire room was ravaged by chimps. Limbs were getting torn apart, the entire room covered in blood and gore. When the only surviving politician witnessed the horrors unfolding around him, he begged the chimps for mercy. One of the chimps lunged at him and tore his intestines out of his body, while everyone is at home, the chimps are preparing their army. I do not have much time left, the random chimp event will happen on-",
                        "https://i.kym-cdn.com/photos/images/newsfeed/001/745/570/c8e.jpg",
                        "https://i.kym-cdn.com/photos/images/newsfeed/001/745/586/7a7.jpg",
                        "https://i.kym-cdn.com/photos/images/newsfeed/001/745/590/a71.jpg",
                        "https://www.youtube.com/watch?v=7Sj1TEbq9GI"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith(tuple(chimpEventTriggers)):
        await message.channel.send(random.choice(chimpEventResponses))


client.run('(TOKEN GOES HERE)')
