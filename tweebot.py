import tweepy
def create_api():
  consumer_key='d12ry2OY8cAH8gLi7Ag7dtPGq'
  consumer_secret='sPRfjN2zzC2tHlRsf94y0JfhK7iVVy3bd4CRY3jqPWo5fqMyyY'
  access_token='1308941177672970240-kWyJ8EQ7Uv361w8AeigKFXKygWVnfZ'
  access_token_secret='XttKkSPob9sHuWpe9pEfS5OaotYFfBq2D70JXsLsrfXv8'
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API CREATED')
  import time
def follower_count(user): 
  emoji_numbers={0:'0️⃣',
                1:'1️⃣',
                2:'2️⃣',
                3:'3️⃣',
                4:'4️⃣',
                5:'5️⃣',
                6:'6️⃣',
                7:'7️⃣',
                8:'8️⃣',
                9:'9️⃣'}
  
  uf_split=[int(i) for i in str(user.followers_count)]
  emoji_followers=''.join([emoji_numbers[j] for j in uf_split  if j in emoji_numbers.keys()])
  return emoji_followers




while True:
    user = api.get_user('Srivats24400149')
    api.update_profile(name=f'Srivatsan|{follower_count(user)} Followers')
    print(f'updating Twitter name: Srivatsan|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
