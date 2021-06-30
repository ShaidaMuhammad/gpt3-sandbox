"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=300)

# Reading dataframe from excel
df = pd.read_excel('examples/messages_and_labels_prepared_for_gpt-3.xlsx')

# Iterating row wise on dataframe
for index, row in df.iterrows():
    gpt.add_example(Example(row['Labels'], row['message']))
    print((row['Labels'], row['message']))

    if index == 30:
        break

# gpt.add_example(Example("establish_credibility, incentive_for_connecting, personalization",
#                         "Hi (name), You're working at (company) I am recruiting for (job_title) position. I think you "
#                         "might be a great fit. best, (name)"))
# gpt.add_example(Example("call_to_action",
#                         "Hi (name), Thank you for connecting with me. As I mentioned I would love to connect via "
#                         "phone. What time works this or next week? Cheers! :) (name)"))
# gpt.add_example(Example("incentive_for_connecting, personalization",
#                         "Hi (name), You're working at (company) I am recruiting for (job_title) position. I think you "
#                         "might be a great fit. best, (name)"))
# gpt.add_example(Example("call_to_action, personalization",
#                         "Hi (name), Are you open to interim tax projects or are you partial to full-time? I see you "
#                         "are currently at (company). Is that in a fulltime or consulting capacity? Would love to "
#                         "connect to see what types of roles, interim or otherwise, you'd like to hear about. (name)"))
# gpt.add_example(Example("call_to_action, establish_credibility. incentive_for_connecting. personalization",
#                         "(name), I recruit executive search consultants responsible for originating new business. Our "
#                         "clients run the gamut from small boutiques to global mid size and the Big 5 search firms - "
#                         "are you open to exploring possible options? Pick a time here "
#                         "pencilit.io/raj/hollanddutchearle/30mins"))
# gpt.add_example(Example("call_to_action, common_ground, establish_credibility, incentive_for_connecting, "
#                         "personalization, flattery",
#                         "Hi (name), I am impressed with your profile as you're working as (job_title) at (job_title) "
#                         "I think you might be the perfect fit for (job_title). Should we connect this week? best ("
#                         "name)"))
# gpt.add_example(Example("personalization",
#                       "Hi (name)"))

# Define UI configuration
config = UIConfig(description="Categories to Have in the message",
                  button_text="Generate Message",
                  placeholder="call_to_action, incentive_for_connecting")

demo_web_app(gpt, config)
