from os import getenv
from .waits.short_wait import short_wait
from .waits.med_wait import med_wait
from .mailer import send_error_email
from tweepy import Cursor, TweepError, API, OAuthHandler
from random import choice


# ---------------------------------------------------------------------------- #
# API key:
api_key = getenv("85ydEkXlBBciiAYLONlPMqVhk")
# API secret key:
api_secret = getenv("QT2RlCWJCybSM98YCAwmjXpUkPGjJvnVA7vnqputXwAv6qLXR4")
# Access token: 
access_token = getenv("1305673102160875523-6bstDMBo5xu0UOdqea3mi5x0uKPSph")
# Access token secret: 
access_token_secret = getenv("7gOQNzknTQDDle6IForuCTpP6WIjRXLh0Y6BrTnSafjAZ")
# ---------------------------------- Tweepy ---------------------------------- #
# Tweepy 0Auth 1a authentication:
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
# API Variable:
api = API(auth, wait_on_rate_limit=True)


# ---------------------------------------------------------------------------- #
def unfollow_nonfollowers(followers, people_i_follow):
    count = choice(range(1, 16))
    for person in people_i_follow:
        if person not in followers:
            try:
                user = api.get_user(person)
                print(f"-> {user.screen_name} not in followers")
                api.destroy_friendship(person)
                print(f"-> Unfollowed @{user.screen_name}...")
                count -= 1
                med_wait()
                if count == 0:
                    return
            except TweepError as error:
                print(f"-> Error: {error.reason}")
                send_error_email.send_error_email(error)
                pass


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    unfollow_nonfollowers()