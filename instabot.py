from instabot import Bot
bot = Bot()
bot.login(username = "anuragsinghok",password= "13234235")
bot.follow('followpersonsuername')# it will folllow the person which username you entered
bot.upload_photo("path_of_photo to upload",caption="i love insta")
bot.unfollow("user name of person to unfollow")
followers = bot.get_user_followers("anuragsinghok") # jiska bhi dena hai follower ki list
for follower in followers:
    print(bot.get_user_info(follower))
#we can add multiple functionality by using inbuild methods/functions of instabot lib.
